# 🚀 GUIDA: Come Generare PDF Modificabili dalla Scheda Web

## 📋 Cosa Serve

Per generare PDF modificabili dalla scheda HTML serve un **server Python locale**.

### Requisiti:
- Python 3.x installato
- Flask (`pip install flask flask-cors`)
- I file di AlicePunk nella stessa cartella

## 🎯 Setup in 3 Passi

### PASSO 1: Installa Flask

Apri il terminale ed esegui:

```bash
pip install flask flask-cors
```

### PASSO 2: Avvia il Server

Nella cartella con i file AlicePunk, esegui:

```bash
python3 server_pdf.py
```

Vedrai:
```
🚀 AlicePunk PDF Server
================================================
📂 Script: /path/to/generate_pdf_MODIFICABILE.py
🌐 Server: http://localhost:5000
🔗 Apri la scheda HTML e usa 'Salva PDF'!
================================================
```

**IMPORTANTE**: Lascia il terminale aperto! Il server deve restare attivo.

### PASSO 3: Usa la Scheda

1. Apri `alicepunk_scheda.html` nel browser
2. Compila il personaggio
3. Clicca **"📄 Salva PDF"**
4. Il PDF modificabile viene scaricato! ✨

## 🎮 Come Funziona

```
[Scheda HTML] 
    ↓ (clicca "Salva PDF")
[Invia dati a http://localhost:5000]
    ↓
[Server Python genera PDF modificabile]
    ↓
[Browser scarica il PDF]
```

## ✅ Verifica che Funzioni

### Test 1: Server Attivo?

Apri nel browser: `http://localhost:5000`

Dovresti vedere: "🌆 AlicePunk PDF Server - Server attivo!"

### Test 2: Genera PDF

1. Apri la scheda HTML
2. Scrivi almeno un nome
3. Clicca "Salva PDF"
4. Dovrebbe scaricare il PDF!

## 🐛 Problemi Comuni

### ❌ "Server non disponibile"

**Causa**: Il server non è avviato
**Soluzione**: 
```bash
python3 server_pdf.py
```

### ❌ "ModuleNotFoundError: No module named 'flask'"

**Causa**: Flask non installato
**Soluzione**:
```bash
pip install flask flask-cors
```

### ❌ "generate_pdf_MODIFICABILE.py non trovato"

**Causa**: I file non sono nella stessa cartella
**Soluzione**: Metti tutti i file nella stessa cartella:
- alicepunk_scheda.html
- server_pdf.py
- generate_pdf_MODIFICABILE.py

### ❌ Porta 5000 già in uso

**Soluzione**: Modifica la porta nel file `server_pdf.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Cambia 5000 → 5001
```

E nell'HTML cambia l'URL:
```javascript
fetch('http://localhost:5001/generate-pdf', {  // 5000 → 5001
```

## 📱 Alternativa SENZA Server

Se non vuoi usare il server:

1. Compila la scheda HTML
2. Clicca **"🖨️ Stampa"**
3. Scegli "Salva come PDF"
4. Il PDF NON sarà modificabile, ma avrà tutti i dati

Oppure:

1. Apri la console del browser (F12)
2. Copia lo script per estrarre dati (vedi README_PDF.md)
3. Salva il JSON in un file
4. Esegui manualmente:
```bash
cat personaggio.json | python3 generate_pdf_MODIFICABILE.py output.pdf
```

## 🌐 Usare Online (Avanzato)

Per usare la scheda online con PDF modificabili, dovresti:

1. Hostare il server su un servizio cloud (Heroku, Railway, ecc.)
2. Modificare l'URL nell'HTML da `localhost:5000` all'URL del server
3. Configurare CORS correttamente

## 💡 Tips

- **Lascia il server sempre attivo** mentre usi la scheda
- Il server si riavvia automaticamente quando modifichi `server_pdf.py`
- Puoi usare la scheda HTML anche offline (auto-save funziona sempre)
- Il PDF modificabile si apre in Adobe Reader, Foxit, Preview (Mac), ecc.

## 📞 Comandi Rapidi

**Avvia server:**
```bash
python3 server_pdf.py
```

**Test server:**
```bash
curl http://localhost:5000/health
```

**Installa dipendenze:**
```bash
pip install flask flask-cors reportlab
```

---

**Fatto!** Ora puoi generare PDF modificabili con un click! 🎉✨
