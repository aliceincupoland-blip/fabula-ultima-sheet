#!/usr/bin/env python3
"""
AlicePunk PDF Generator - VERSIONE SEMPLICE
Genera PDF statici (NON modificabili) - più compatibili
"""

import sys
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor

def create_pdf(data, output_path):
    """Crea un PDF semplice e compatibile"""
    
    # Colori
    pink = HexColor('#ff006e')
    cyan = HexColor('#00d9ff')
    purple = HexColor('#8b00ff')
    bg = HexColor('#f5f5fa')
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # Background
    c.setFillColor(bg)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Header
    c.setFillColor(pink)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(width/2, height - 60, "ALICEPUNK")
    
    c.setFillColor(HexColor('#333333'))
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height - 85, "Sistema d10 Pool - Scheda Personaggio")
    
    c.setStrokeColor(pink)
    c.setLineWidth(4)
    c.line(50, height - 100, width - 50, height - 100)
    
    y = height - 140
    x = 60
    
    # IDENTITÀ
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "1. IDENTITÀ")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 11)
    c.drawString(x + 10, y, f"Nome: {data.get('name', '_______________')}")
    y -= 20
    c.drawString(x + 10, y, f"Classe: {data.get('class', '_______________').upper()}")
    y -= 20
    c.drawString(x + 10, y, f"Concetto: {data.get('concept', '_______________')}")
    
    y -= 30
    
    # ABILITÀ
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "2. ABILITÀ DI CLASSE")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 10)
    skills = data.get('skills', [])
    for skill in skills[:2]:
        c.drawString(x + 10, y, f"• {skill}")
        y -= 18
    
    if not skills:
        c.drawString(x + 10, y, "• Nessuna abilità selezionata")
        y -= 18
    
    y -= 20
    
    # POOL
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "3. POOL DI DADI")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 10)
    pool_map = {
        'balanced': '⚖️ BILANCIATO (3,3,2,2,0)',
        'specialist': '⭐ SPECIALISTA (4,3,2,1,0)',
        'extreme': '💥 ESTREMO (5,3,2,0,0)'
    }
    c.drawString(x + 10, y, pool_map.get(data.get('pool', ''), 'Non selezionato'))
    
    y -= 30
    
    # APPROCCI
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "4. APPROCCI")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 11)
    
    # Prima riga
    muscoli = data.get('muscoli', '0')
    punk = data.get('punk', '0')
    social = data.get('social', '0')
    c.drawString(x + 10, y, f"MUSCOLI: {muscoli}d10     PUNK: {punk}d10     SOCIAL: {social}d10")
    y -= 20
    
    # Seconda riga
    velocita = data.get('velocita', '0')
    mente = data.get('mente', '0')
    c.drawString(x + 10, y, f"VELOCITÀ: {velocita}d10    MENTE: {mente}d10")
    
    y -= 30
    
    # CYBERWARE
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "5. CYBERWARE")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 9)
    cyberware = data.get('cyberware', [])
    if cyberware:
        for cw in cyberware[:5]:
            c.drawString(x + 10, y, f"• {cw}")
            y -= 15
    else:
        c.drawString(x + 10, y, "• Nessun cyberware")
        y -= 15
    
    y -= 20
    
    # CONDIZIONE
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "6. CONDIZIONE")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 10)
    c.drawString(x + 10, y, "DANNO:  ☐ ☐ ☐ ☐ ☐ ☐ ☐ ☐  (A 8 sei KO)")
    y -= 20
    c.drawString(x + 10, y, "STRESS: ☐ ☐ ☐ ☐  (A 4 agisci disperato)")
    
    y -= 30
    
    # EQUIPAGGIAMENTO
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "7. EQUIPAGGIAMENTO")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 9)
    equipment = data.get('equipment', 'Nessun equipaggiamento')
    # Split in righe se troppo lungo
    if len(equipment) > 70:
        words = equipment.split()
        line = ""
        for word in words:
            if len(line + word) < 70:
                line += word + " "
            else:
                c.drawString(x + 10, y, line.strip())
                y -= 15
                line = word + " "
        if line:
            c.drawString(x + 10, y, line.strip())
            y -= 15
    else:
        c.drawString(x + 10, y, equipment)
        y -= 15
    
    y -= 20
    
    # CREDITI
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "8. CREDITI")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 11)
    c.drawString(x + 10, y, f"{data.get('credits', '0')}₡")
    
    y -= 30
    
    # BACKGROUND
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x, y, "9. BACKGROUND")
    y -= 25
    
    c.setFillColor(HexColor('#000000'))
    c.setFont("Helvetica", 9)
    background = data.get('background', '')
    if background:
        if len(background) > 70:
            words = background.split()
            line = ""
            for word in words:
                if len(line + word) < 70:
                    line += word + " "
                else:
                    c.drawString(x + 10, y, line.strip())
                    y -= 13
                    line = word + " "
            if line:
                c.drawString(x + 10, y, line.strip())
                y -= 13
        else:
            c.drawString(x + 10, y, background)
            y -= 13
    
    contacts = data.get('contacts', '')
    if contacts:
        c.drawString(x + 10, y, f"Contatti: {contacts}")
    
    y -= 35
    
    # REGOLE
    if y > 100:
        c.setFillColor(cyan)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, "REGOLE")
        y -= 20
        
        c.setFillColor(HexColor('#000000'))
        c.setFont("Helvetica", 8)
        c.drawString(x + 10, y, "Sistema: 1.Scegli approccio | 2.Tira Nd10 | 3.Conta 6+ = successi")
        y -= 13
        c.drawString(x + 10, y, "Risultati: 0=Critico- | 1=Scegli complicazione | 2=Parziale | 3-4=Ok | 5+=Critico (+1 XP)")
        y -= 13
        c.drawString(x + 10, y, "Combattimento: Attacco vs Difesa | Danno = arma - armatura")
    
    # Footer
    c.setFillColor(HexColor('#999999'))
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width/2, 40, "AlicePunk - Sistema d10 Pool")
    
    c.save()
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = "/mnt/user-data/outputs/personaggio.pdf"
    
    data = json.load(sys.stdin)
    create_pdf(data, output_path)
    print(f"✅ PDF creato: {output_path}")
