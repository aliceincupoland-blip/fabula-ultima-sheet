# 🌆 ALICEPUNK - Kit Completo

**Sistema d10 Pool per Play-by-Chat**

## 📦 Contenuto del Kit

### 🎮 File Principali

1. **alicepunk_scheda.html** - Scheda personaggio interattiva
   - Auto-save in localStorage
   - 8 classi giocabili
   - 5 approcci
   - 10 cyberware
   - Gestione completa personaggio
   - Stampabile

2. **alicepunk_esempio.pdf** - PDF di esempio
   - Background sfumato
   - Layout pulito e professionale
   - Pronto da stampare o usare digitalmente
   - **NOTA**: PDF statico (non modificabile) per massima compatibilità

3. **generate_pdf.py** - Generatore PDF Python
   - Crea PDF statici da dati JSON
   - Layout professionale con background sfumato
   - **PDF non modificabile** ma perfettamente compatibile
   - **SENZA sezione XP** (come richiesto)

4. **README_PDF.md** - Guida dettagliata per generare PDF

## 🚀 Quick Start

### 1. Usa la Scheda HTML

Apri `alicepunk_scheda.html` nel browser e:

1. Compila il personaggio
2. Tutto si salva automaticamente
3. Usa **🖨️ Stampa** per salvare come PDF

### 2. Genera PDF Modificabile

**Metodo Veloce:**
```bash
# Crea un file con i dati del tuo personaggio
cat > mio_pg.json << 'EOF'
{
  "name": "Il Tuo Nome",
  "class": "netrunner",
  "concept": "Il tuo concetto",
  "skills": ["Abilità 1", "Abilità 2"],
  "pool": "specialist",
  "muscoli": "1",
  "punk": "4",
  "social": "2",
  "velocita": "3",
  "mente": "0",
  "cyberware": ["Cyberware 1", "Cyberware 2"],
  "equipment": "Il tuo equipaggiamento",
  "credits": "1500",
  "background": "La tua storia",
  "contacts": "I tuoi contatti"
}
EOF

# Genera il PDF
cat mio_pg.json | python3 generate_pdf.py mio_personaggio.pdf
```

**Metodo da Browser:**

1. Compila la scheda HTML
2. Apri console (F12)
3. Copia e incolla il codice dal README_PDF.md
4. Salva l'output JSON
5. Genera il PDF con lo script sopra

## 🎯 Sistema di Gioco

### 🎲 Meccanica Base
1. **Scegli un approccio** (Muscoli, Punk, Social, Velocità, Mente)
2. **Tira Nd10** (N = valore dell'approccio)
3. **Conta successi** (ogni dado 6+ = 1 successo)

### 📊 Risultati
- **0 successi** = Critico negativo
- **1 successo** = Tu scegli cosa va male
- **2 successi** = Successo parziale (con costo)
- **3-4 successi** = Successo
- **5+ successi** = Critico! (+1 XP)

### ⚔️ Combattimento
- Attacco vs Difesa (entrambi tirano)
- **Danno** = danni arma - armatura nemica
- **8 Danno** = KO
- **4 Stress** = Agisci disperato

## 🎭 8 Classi Giocabili

1. **⚡ Netrunner** - Hacker della rete
2. **⚔️ Solitario** - Combattente solitario
3. **💼 Corporativo** - Potere aziendale
4. **🏍️ Nomade** - Famiglia delle lande
5. **🏥 Medtech** - Dottore cybernetico
6. **🤝 Fixer** - Mediatore e mercante
7. **💭 Dreamer** - Fantasma digitale
8. **⚔️ Ronin** - Guerriero Bushido

Ogni classe ha **5 abilità speciali** (scegline 2).

## 💰 Economia

**Crediti Iniziali:** `4d10 × 100 + 600₡ + Bonus Classe`

**Bonus per Classe:**
- Netrunner: +100₡
- Solitario: +50₡
- Corporativo: +400₡ (più ricco!)
- Nomade: +0₡ (più povero)
- Medtech: +150₡
- Fixer: +300₡
- Dreamer: +200₡
- Ronin: +100₡

**Range:** 1000-4600₡ + bonus

## 🛠️ Requisiti Tecnici

### Per usare la Scheda HTML:
- Qualsiasi browser moderno
- Nessuna installazione necessaria

### Per generare PDF:
```bash
pip install reportlab
```

## 📝 Caratteristiche PDF

✅ **Layout Professionale:**
- Background sfumato (non più bianco!)
- Tutte le info del personaggio
- Checkbox ☐ per Danno e Stress (da spuntare a mano o digitalmente)

✅ **Contenuto Completo:**
- Identità (Nome, Classe, Concetto)
- Abilità di classe
- Pool e Approcci
- Cyberware
- Equipaggiamento
- Crediti
- Background e Contatti
- Regole di gioco

✅ **PDF Statico** (non modificabile):
- Massima compatibilità con tutti i lettori PDF
- Funziona ovunque (mobile, desktop, tablet)
- Leggero e veloce (3KB)
- Perfetto per stampa

**NOTA**: Il PDF generato contiene tutti i dati ma NON è modificabile.
Per modificare, usa la scheda HTML e rigenera il PDF!

## 🎨 Features della Scheda HTML

- ✨ Auto-save automatico in localStorage
- 🎯 Validazione scelte (max 2 abilità)
- 📱 Responsive (mobile-friendly)
- 🖨️ Stampabile
- 🎨 Design cyberpunk con gradienti
- 💾 Bottone "Cancella" per reset
- 📊 Tabelle prezzi integrate
- 🔧 Sezione cyberware con 10 opzioni
- 📝 Note approcci compilabili

## 💡 Tips & Tricks

1. **Backup:** La scheda HTML salva automaticamente, ma fai backup del PDF!
2. **Mobile:** Funziona benissimo su tablet con PDF reader
3. **Stampa:** Puoi sempre stampare la scheda HTML come PDF
4. **Modifiche:** Il PDF è completamente editabile in Adobe Reader, Foxit, Preview (Mac)

## 🐛 Troubleshooting

**Il PDF non si apre:**
- Prova con un altro PDF reader
- Usa "Stampa → Salva come PDF" dalla scheda HTML come alternativa

**I dati non si salvano:**
- Controlla che il browser non sia in modalità incognito
- localStorage deve essere abilitato

**Lo script Python non funziona:**
- Verifica di avere Python 3.x
- Installa reportlab: `pip install reportlab`
- Controlla che il JSON sia valido

## 📖 Documentazione Aggiuntiva

Vedi **README_PDF.md** per:
- Istruzioni dettagliate generazione PDF
- Script JavaScript per estrarre dati
- Esempi completi

## 🎮 Inizia a Giocare!

1. Apri `alicepunk_scheda.html`
2. Crea il tuo personaggio
3. Stampa/Esporta il PDF
4. Inizia la tua avventura cyberpunk!

---

**ALICEPUNK** - Sistema d10 Pool
*Hack it, fallo tuo!* 🌆⚡💜

Versione: 2.0 Final
Data: Febbraio 2026
