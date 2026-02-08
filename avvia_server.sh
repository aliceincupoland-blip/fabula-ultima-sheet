#!/bin/bash
# AlicePunk PDF Server - Avvio Rapido

echo "🌆 ALICEPUNK PDF Server - Avvio"
echo "================================"
echo ""

# Controlla Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 non trovato!"
    echo "   Installa Python 3 da https://www.python.org"
    exit 1
fi

echo "✅ Python 3 trovato"

# Controlla Flask
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installo Flask..."
    pip install flask flask-cors
    
    if [ $? -ne 0 ]; then
        echo "❌ Errore installazione Flask"
        echo "   Prova manualmente: pip install flask flask-cors"
        exit 1
    fi
fi

echo "✅ Flask installato"
echo ""

# Controlla che lo script esista
if [ ! -f "generate_pdf_MODIFICABILE.py" ]; then
    echo "⚠️  File generate_pdf_MODIFICABILE.py non trovato!"
    echo "   Assicurati di essere nella cartella giusta."
    exit 1
fi

echo "🚀 Avvio server..."
echo "================================"
echo ""
echo "📍 Server: http://localhost:5000"
echo "📄 Apri alicepunk_scheda.html e clicca 'Salva PDF'"
echo ""
echo "⏹️  Premi CTRL+C per fermare"
echo ""

# Avvia il server
python3 server_pdf.py
