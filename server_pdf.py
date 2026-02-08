#!/usr/bin/env python3
"""
AlicePunk PDF Server
Mini server Flask per generare PDF modificabili dalla scheda web
"""

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import json
import tempfile
import os
import subprocess
import sys

app = Flask(__name__)
CORS(app)  # Permetti richieste da qualsiasi origine

# Path allo script generatore
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATOR_SCRIPT = os.path.join(SCRIPT_DIR, 'generate_pdf_MODIFICABILE.py')

@app.route('/')
def home():
    return """
    <h1>🌆 AlicePunk PDF Server</h1>
    <p>Server attivo! Ora puoi usare il bottone "Salva PDF" nella scheda HTML.</p>
    <p>Endpoint: <code>POST /generate-pdf</code></p>
    """

@app.route('/generate-pdf', methods=['POST', 'OPTIONS'])
def generate_pdf():
    """Genera PDF modificabile dai dati della scheda"""
    
    # Gestisci preflight CORS
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    try:
        # Ottieni i dati
        if request.is_json:
            data = request.get_json()
        else:
            data_str = request.form.get('data')
            if data_str:
                data = json.loads(data_str)
            else:
                return jsonify({'error': 'No data provided'}), 400
        
        print(f"📝 Ricevuto: {data.get('name', 'Unknown')}")
        
        # Crea file temporaneo per il PDF
        fd, pdf_path = tempfile.mkstemp(suffix='.pdf', prefix='alicepunk_')
        os.close(fd)
        
        # Chiama lo script Python per generare il PDF
        process = subprocess.Popen(
            [sys.executable, GENERATOR_SCRIPT, pdf_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        stdout, stderr = process.communicate(input=json.dumps(data).encode('utf-8'))
        
        if process.returncode != 0:
            print(f"❌ Errore: {stderr.decode()}")
            return jsonify({'error': stderr.decode()}), 500
        
        print(f"✅ PDF creato: {pdf_path}")
        
        # Nome file per il download
        char_name = data.get('name', 'personaggio').replace(' ', '_')
        download_name = f"alicepunk_{char_name}.pdf"
        
        # Invia il PDF al client
        return send_file(
            pdf_path,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=download_name
        )
        
    except Exception as e:
        print(f"❌ Errore generale: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Endpoint per verificare che il server sia attivo"""
    return jsonify({'status': 'ok', 'message': 'Server attivo!'})

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 AlicePunk PDF Server")
    print("=" * 60)
    print(f"📂 Script: {GENERATOR_SCRIPT}")
    print(f"🌐 Server: http://localhost:5000")
    print(f"🔗 Apri la scheda HTML e usa 'Salva PDF'!")
    print("=" * 60)
    
    # Verifica che lo script esista
    if not os.path.exists(GENERATOR_SCRIPT):
        print(f"⚠️  ATTENZIONE: {GENERATOR_SCRIPT} non trovato!")
        print(f"   Assicurati che sia nella stessa cartella di questo script.")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
