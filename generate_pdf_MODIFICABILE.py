#!/usr/bin/env python3
"""
AlicePunk PDF Generator - CON CAMPI MODIFICABILI
Versione robusta con form fields funzionanti
"""

import sys
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfbase import pdfform

def create_fillable_pdf(data, output_path):
    """Crea PDF con campi modificabili"""
    
    pink = HexColor('#ff006e')
    purple = HexColor('#8b00ff')
    cyan = HexColor('#00d9ff')
    bg = HexColor('#f8f8fc')
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # Background sfumato
    c.setFillColor(bg)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    
    # Header
    c.setFillColor(pink)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(width/2, height - 55, "ALICEPUNK")
    
    c.setFillColor(black)
    c.setFont("Helvetica", 11)
    c.drawCentredString(width/2, height - 75, "Sistema d10 Pool - Scheda Modificabile")
    
    c.setStrokeColor(pink)
    c.setLineWidth(3)
    c.line(50, height - 90, width - 50, height - 90)
    
    y = height - 120
    x = 60
    
    # Form object
    form = c.acroForm
    
    # === IDENTITÀ ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "1. IDENTITÀ")
    y -= 25
    
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    
    # Nome (campo editabile)
    c.drawString(x + 5, y, "Nome:")
    form.textfield(
        name='nome',
        tooltip='Il tuo nome o alias',
        x=x + 50,
        y=y - 6,
        width=180,
        height=16,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('name', '')
    )
    y -= 22
    
    # Classe (campo editabile)
    c.drawString(x + 5, y, "Classe:")
    form.textfield(
        name='classe',
        tooltip='La tua classe',
        x=x + 50,
        y=y - 6,
        width=180,
        height=16,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('class', '')
    )
    y -= 22
    
    # Concetto (campo editabile lungo)
    c.drawString(x + 5, y, "Concetto:")
    form.textfield(
        name='concetto',
        tooltip='Il concetto del personaggio',
        x=x + 5,
        y=y - 22,
        width=400,
        height=16,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('concept', '')
    )
    y -= 38
    
    # === ABILITÀ (testo fisso) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "2. ABILITÀ DI CLASSE")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    skills = data.get('skills', [])
    for skill in skills[:2]:
        c.drawString(x + 5, y, f"• {skill}")
        y -= 14
    if not skills:
        c.drawString(x + 5, y, "• Nessuna abilità")
        y -= 14
    
    y -= 15
    
    # === APPROCCI (testo fisso) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "3. APPROCCI")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(x + 5, y, f"MUSCOLI: {data.get('muscoli', '0')}d10  |  PUNK: {data.get('punk', '0')}d10  |  SOCIAL: {data.get('social', '0')}d10")
    y -= 14
    c.drawString(x + 5, y, f"VELOCITÀ: {data.get('velocita', '0')}d10  |  MENTE: {data.get('mente', '0')}d10")
    y -= 25
    
    # === CONDIZIONE (checkboxes) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "4. CONDIZIONE")
    y -= 22
    
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(x + 5, y, "DANNO:")
    
    # 8 checkbox per danno
    for i in range(8):
        form.checkbox(
            name=f'danno{i+1}',
            tooltip=f'Danno {i+1}',
            x=x + 60 + (i * 22),
            y=y - 5,
            size=14,
            borderWidth=1,
            borderColor=HexColor('#cc0000'),
            fillColor=white,
            checked=False,
            forceBorder=True
        )
    
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor('#666666'))
    c.drawString(x + 240, y, "(A 8 = KO)")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 9)
    c.drawString(x + 5, y, "STRESS:")
    
    # 4 checkbox per stress
    for i in range(4):
        form.checkbox(
            name=f'stress{i+1}',
            tooltip=f'Stress {i+1}',
            x=x + 60 + (i * 22),
            y=y - 5,
            size=14,
            borderWidth=1,
            borderColor=HexColor('#ff6b35'),
            fillColor=white,
            checked=False,
            forceBorder=True
        )
    
    c.setFont("Helvetica", 7)
    c.setFillColor(HexColor('#666666'))
    c.drawString(x + 150, y, "(A 4 = Disperato)")
    y -= 28
    
    # === EQUIPAGGIAMENTO (campo editabile) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "5. EQUIPAGGIAMENTO")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 8)
    form.textfield(
        name='equipaggiamento',
        tooltip='Il tuo equipaggiamento',
        x=x + 5,
        y=y - 40,
        width=400,
        height=35,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('equipment', '')
    )
    y -= 50
    
    # === CREDITI (campo editabile) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "6. CREDITI")
    y -= 22
    
    c.setFillColor(black)
    c.setFont("Helvetica", 10)
    c.drawString(x + 5, y, "Crediti:")
    form.textfield(
        name='crediti',
        tooltip='I tuoi crediti',
        x=x + 60,
        y=y - 6,
        width=80,
        height=16,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=str(data.get('credits', '0'))
    )
    c.drawString(x + 145, y, "₡")
    y -= 28
    
    # === BACKGROUND (campo editabile) ===
    c.setFillColor(purple)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(x, y, "7. BACKGROUND")
    y -= 20
    
    c.setFillColor(black)
    c.setFont("Helvetica", 8)
    c.drawString(x + 5, y, "Storia:")
    form.textfield(
        name='storia',
        tooltip='La tua storia',
        x=x + 5,
        y=y - 35,
        width=400,
        height=30,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('background', '')
    )
    y -= 45
    
    c.drawString(x + 5, y, "Contatti:")
    form.textfield(
        name='contatti',
        tooltip='I tuoi contatti',
        x=x + 60,
        y=y - 6,
        width=340,
        height=16,
        borderWidth=1,
        borderColor=pink,
        fillColor=white,
        textColor=black,
        forceBorder=True,
        value=data.get('contacts', '')
    )
    y -= 30
    
    # === REGOLE ===
    c.setFillColor(cyan)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x, y, "REGOLE")
    y -= 16
    
    c.setFillColor(black)
    c.setFont("Helvetica", 7)
    c.drawString(x + 5, y, "Sistema: 1.Approccio | 2.Nd10 | 3.Conta 6+=successi")
    y -= 11
    c.drawString(x + 5, y, "0=Crit- | 1=Scegli problema | 2=Parziale | 3-4=Ok | 5+=Crit (+1 XP)")
    y -= 11
    c.drawString(x + 5, y, "Combattimento: Attacco vs Difesa | Danno=arma-armatura")
    
    # Footer
    c.setFillColor(HexColor('#999999'))
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, 35, "AlicePunk - PDF Modificabile")
    
    c.save()
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = "/mnt/user-data/outputs/personaggio_modificabile.pdf"
    
    data = json.load(sys.stdin)
    create_fillable_pdf(data, output_path)
    print(f"✅ PDF modificabile creato: {output_path}")
