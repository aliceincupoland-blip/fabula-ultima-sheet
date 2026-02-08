# AlicePunk - Generatore PDF

## 📄 Come Generare un PDF Modificabile

Il sistema include un generatore Python che crea PDF con campi editabili (SENZA sezione XP).

### Opzione 1: Da Riga di Comando (Manuale)

1. Compila la scheda HTML normalmente
2. Apri la console del browser (F12)
3. Copia questo codice nella console per estrarre i dati:

```javascript
const data = {
    name: document.getElementById('name')?.value || '',
    class: document.querySelector('input[name="class"]:checked')?.value || '',
    concept: document.getElementById('concept')?.value || '',
    skills: Array.from(document.querySelectorAll('.skill-checkbox input:checked')).map(cb => cb.nextElementSibling?.querySelector('.skill-name')?.textContent).filter(Boolean),
    pool: document.querySelector('input[name="pool"]:checked')?.value || '',
    muscoli: document.getElementById('muscoli')?.value || '0',
    punk: document.getElementById('punk')?.value || '0',
    social: document.getElementById('social')?.value || '0',
    velocita: document.getElementById('velocita')?.value || '0',
    mente: document.getElementById('mente')?.value || '0',
    cyberware: Array.from(document.querySelectorAll('.cyber-item input:checked')).map(cb => cb.nextElementSibling?.querySelector('.cyber-title')?.textContent).filter(Boolean),
    equipment: document.getElementById('equipment')?.value || '',
    credits: document.getElementById('credits')?.value || '0',
    background: document.getElementById('background')?.value || '',
    contacts: document.getElementById('contacts')?.value || ''
};
console.log(JSON.stringify(data, null, 2));
```

4. Copia l'output JSON
5. Salvalo in un file `character.json`
6. Esegui:

```bash
cat character.json | python3 generate_pdf.py output.pdf
```

### Opzione 2: Server Web (Automatico)

**NOTA**: Questa funzionalità richiede un server locale Python.

1. Avvia il server (se disponibile):
```bash
python3 pdf_server.py
```

2. Il server sarà disponibile su `http://localhost:5000`

3. La scheda HTML può ora generare PDF cliccando "Salva PDF"

### Opzione 3: Stampa come PDF (Più Semplice)

Per ora, il metodo più semplice è:

1. Compila la scheda HTML
2. Clicca su "🖨️ Stampa"
3. Scegli "Salva come PDF" come stampante
4. Il PDF non sarà modificabile ma conterrà tutti i dati

## 📝 Caratteristiche del PDF Generato

✅ Campi modificabili per: Nome, Concetto, Inventario, Crediti, Storia, Contatti
✅ Checkbox modificabili per: Danno (8), Stress (4)
✅ Dati fissi (già scelti): Classe, Abilità, Pool, Approcci, Cyberware
✅ Layout a 2 colonne compatto
✅ **SENZA sezione XP** (come richiesto)
✅ Regole incluse in basso

## 🛠️ Requisiti

- Python 3.x
- reportlab (`pip install reportlab`)

## 📦 File Inclusi

- `alicepunk_scheda.html` - Scheda interattiva web
- `generate_pdf.py` - Generatore PDF Python
- `test_character.pdf` - Esempio di PDF generato
- `README_PDF.md` - Questo file

## 💡 Tips

- Il PDF è completamente modificabile in Adobe Acrobat, Foxit, Preview (Mac), ecc.
- I campi checkbox possono essere spuntati/despuntati nel PDF
- Perfetto per giocare con PDF reader su tablet!

---

**AlicePunk** - Sistema d10 Pool | Hack it, fallo tuo! 🌆⚡
