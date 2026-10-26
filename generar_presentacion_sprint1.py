"""
Generador de Presentación Ejecutiva y Académica del Sprint 1 para Caleta.
Materia: Herramientas Ágiles para Reuniones
Estructura: EXACTAMENTE 8 DIAPOSITIVAS Widescreen 16:9.
Mejoras clave:
- Marcos estéticos integrados con bordes redondeados y badges armónicos (sin barras toscas superpuestas).
- Textos adaptados con márgenes internos de respiración, tamaños proporcionados y sin desbordes.
- Marcos de navegador (mockup con controles circulares y barra URL) para las capturas del programa.
- Paleta fintech curada y consistente.
"""

import os
import subprocess
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- PALETA DE COLORES CALETA (Fintech Moderna) ---
C_DARK_NAVY  = RGBColor(11, 19, 43)     # #0B132B - Fondo oscuro premium
C_SLATE_CARD = RGBColor(20, 31, 56)     # #141F38 - Tarjeta oscura
C_SLATE_BORD = RGBColor(45, 60, 92)     # #2D3C5C - Borde oscuro elegante
C_TEAL_BRAND = RGBColor(13, 148, 136)   # #0D9488 - Esmeralda Caleta
C_TEAL_LIGHT = RGBColor(240, 253, 250)  # #F0FDFA - Chip fondo claro
C_CYAN_ACC   = RGBColor(2, 132, 199)    # #0284C7 - Azul Cyan
C_CYAN_LIGHT = RGBColor(240, 249, 255)  # #F0F9FF
C_PURPLE_ACC = RGBColor(147, 51, 234)   # #9333EA
C_PURPLE_LT  = RGBColor(250, 245, 255)  # #FAF5FF
C_AMBER_ACC  = RGBColor(217, 119, 6)    # #D97706
C_AMBER_LT   = RGBColor(254, 243, 199)  # #FEF3C7
C_GREEN_OK   = RGBColor(16, 185, 129)   # #10B981 - Badge Completado
C_GREEN_LT   = RGBColor(236, 253, 245)  # #ECFDF5
C_RED_ACC    = RGBColor(239, 68, 68)    # #EF4444
C_RED_LT     = RGBColor(254, 242, 242)  # #FEF2F2

C_TEXT_DARK  = RGBColor(15, 23, 42)     # #0F172A - Titulares en fondo claro
C_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B - Texto secundario
C_BG_LIGHT   = RGBColor(248, 250, 252)  # #F8FAFC - Fondo de diapositivas claras
C_BORDER     = RGBColor(226, 232, 240)  # #E2E8F0 - Borde suave
C_WHITE      = RGBColor(255, 255, 255)

# --- RUTAS DE ACTIVOS ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
ENTREGABLES_DIR = os.path.join(BASE_DIR, "entregables")
os.makedirs(ENTREGABLES_DIR, exist_ok=True)

IMG_BURNDOWN = os.path.join(ASSETS_DIR, "burndown_sprint1.png")
IMG_ARQ = os.path.join(ASSETS_DIR, "diagrama_arquitectura.png")
IMG_FONDOS = os.path.join(ASSETS_DIR, "diagrama_flujo_fondos.png")
IMG_LANDING = os.path.join(ASSETS_DIR, "pantalla_registro.png") # Landing page real
IMG_REGISTRO = os.path.join(ASSETS_DIR, "pantalla_landing.png")  # Formulario de registro real

FONT_FAMILY = "Segoe UI"


def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, dark_mode=False):
        """Encabezado refinado, con acento sutil y espaciado proporcional."""
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_TEAL_BRAND
        top_bar.line.fill.background()

        tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.30), Inches(11.5), Inches(0.28))
        tf_tag = tb_tag.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_TEAL_BRAND

        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.58), Inches(11.5), Inches(0.55))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_TEXT_DARK if not dark_mode else C_WHITE

    def add_footer(slide, current_num, total=8, dark_mode=False):
        """Pie de página limpio y discreto."""
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(7.08), Inches(11.733), Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = "Herramientas Ágiles para Reuniones  •  Caleta: Plataforma de Cobros Internacionales  •  Sprint 1"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(8.5)
        p.font.color.rgb = C_TEXT_MUTED if not dark_mode else RGBColor(148, 163, 184)
        
        p_num = tf.add_paragraph()
        p_num.text = f"{current_num} / {total}"
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.font.name = FONT_FAMILY
        p_num.font.size = Pt(8.5)
        p_num.font.bold = True
        p_num.font.color.rgb = C_TEXT_MUTED if not dark_mode else RGBColor(148, 163, 184)

    # =========================================================================
    # SLIDE 1: PORTADA KEYNOTE (Fondo Oscuro Premium #0B132B)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1, C_DARK_NAVY)

    # Acento superior verde marca
    bar1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.1))
    bar1.fill.solid()
    bar1.fill.fore_color.rgb = C_TEAL_BRAND
    bar1.line.fill.background()

    # Badge de la Asignatura con bordes redondeados y estilo moderno
    chip = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.65), Inches(4.3), Inches(0.36))
    chip.fill.solid()
    chip.fill.fore_color.rgb = RGBColor(20, 31, 56)
    chip.line.color.rgb = C_TEAL_BRAND
    chip.line.width = Pt(1.2)
    tf_c = chip.text_frame
    tf_c.margin_top = Inches(0.04)
    p_c = tf_c.paragraphs[0]
    p_c.text = "HERRAMIENTAS ÁGILES PARA REUNIONES"
    p_c.font.name = FONT_FAMILY
    p_c.font.size = Pt(8.5)
    p_c.font.bold = True
    p_c.font.color.rgb = C_TEAL_BRAND
    p_c.alignment = PP_ALIGN.CENTER

    # Título Principal y Subtítulos
    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(1.15), Inches(11.5), Inches(1.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_top = 0
    p1 = tf1.paragraphs[0]
    p1.text = "Caleta."
    p1.font.name = FONT_FAMILY
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE

    p1_sub = tf1.add_paragraph()
    p1_sub.text = "Plataforma de Cobros Internacionales con Liquidación Local para Ecuador"
    p1_sub.font.name = FONT_FAMILY
    p1_sub.font.size = Pt(16)
    p1_sub.font.color.rgb = RGBColor(203, 213, 225)
    p1_sub.space_before = Pt(2)

    p1_goal = tf1.add_paragraph()
    p1_goal.text = "Revisión del Incremento Base de Software — Cierre del Sprint 1"
    p1_goal.font.name = FONT_FAMILY
    p1_goal.font.size = Pt(11.5)
    p1_goal.font.bold = True
    p1_goal.font.color.rgb = C_TEAL_BRAND
    p1_goal.space_before = Pt(4)

    # Institución y Docente (Sin detallar carrera)
    tb_inst = s1.shapes.add_textbox(Inches(0.8), Inches(2.72), Inches(11.5), Inches(0.4))
    tf_inst = tb_inst.text_frame
    p_inst = tf_inst.paragraphs[0]
    p_inst.text = "Universidad Espíritu Santo (UEES)  •  Docente: Marco Vinicio Sotomayor Sánchez"
    p_inst.font.name = FONT_FAMILY
    p_inst.font.size = Pt(9.5)
    p_inst.font.color.rgb = RGBColor(148, 163, 184)

    # 4 Tarjetas de Integrantes con Marco Armónico Completo (Borde coloreado y pill badge)
    team_members = [
        ("Emilio Zúñiga", "PRODUCT OWNER", "Visión del producto, Product Backlog, criterios de aceptación y modelo de comisiones.", C_TEAL_BRAND),
        ("Romina Sigcho", "SCRUM MASTER", "Facilitación de reuniones ágiles, diseño UX/UI, aseguramiento del DoD y actas.", C_CYAN_ACC),
        ("Jeickol Moreira", "BACKEND & PAGOS", "Supabase Auth SSR, RLS en PostgreSQL, triggers atómicos y arquitectura de seguridad.", C_PURPLE_ACC),
        ("Cristhian Grunauer", "FRONTEND & DEVOPS", "Next.js 16, Tailwind CSS v4, Vercel y automatización de CI en GitHub Actions.", C_AMBER_ACC)
    ]

    card_w = Inches(2.78)
    card_h = Inches(3.15)
    start_x = Inches(0.8)
    gap_x = Inches(0.2)
    y_cards = Inches(3.40)

    for i, (name, role, desc, color_role) in enumerate(team_members):
        cx = start_x + i * (card_w + gap_x)
        
        # Tarjeta redondeada con borde sutil coloreado
        c_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, y_cards, card_w, card_h)
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = C_SLATE_CARD
        c_shape.line.color.rgb = color_role
        c_shape.line.width = Pt(1.2)

        # Pill badge superior integrado dentro de la tarjeta
        pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.2), y_cards + Inches(0.2), card_w - Inches(0.4), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(15, 23, 42)
        pill.line.color.rgb = color_role
        pill.line.width = Pt(1)
        tf_pill = pill.text_frame
        tf_pill.margin_top = Inches(0.03)
        p_p = tf_pill.paragraphs[0]
        p_p.text = role
        p_p.font.name = FONT_FAMILY
        p_p.font.size = Pt(8.5)
        p_p.font.bold = True
        p_p.font.color.rgb = color_role
        p_p.alignment = PP_ALIGN.CENTER

        # Contenido de texto adaptado
        tb_m = s1.shapes.add_textbox(cx + Inches(0.2), y_cards + Inches(0.65), card_w - Inches(0.4), card_h - Inches(0.8))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_right = tf_m.margin_top = 0

        p_name = tf_m.paragraphs[0]
        p_name.text = name
        p_name.font.name = FONT_FAMILY
        p_name.font.size = Pt(13)
        p_name.font.bold = True
        p_name.font.color.rgb = C_WHITE
        p_name.space_after = Pt(8)

        p_desc = tf_m.add_paragraph()
        p_desc.text = desc
        p_desc.font.name = FONT_FAMILY
        p_desc.font.size = Pt(9)
        p_desc.font.color.rgb = RGBColor(203, 213, 225)

    add_footer(s1, 1, 8, dark_mode=True)

    # =========================================================================
    # SLIDE 2: PROBLEMA Y SOLUCIÓN (Limpio, 2 Columnas de Alto Impacto)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2, C_BG_LIGHT)
    add_header(s2, "01. Contexto & Propuesta de Valor", "El Reto del Freelancer Ecuatoriano y la Solución Caleta")

    left_x = Inches(0.8)
    left_w = Inches(5.6)
    
    # 3 Tarjetas del Problema con marco integrado armónico
    probs = [
        ("🚫 Stripe no opera en Ecuador", 
         "No admite vinculación a bancos ecuatorianos; obliga a profesionales a crear LLCs costosas en EE.UU. o perder contratos.", C_RED_ACC, C_RED_LT),
        ("💸 Altas comisiones en PayPal", 
         "Retiene 5.4% + $0.30 por cobro, sumado a pérdidas adicionales en intermediarios informales para retirar el efectivo.", C_AMBER_ACC, C_AMBER_LT),
        ("🏦 Tarifas fijas en transferencias SWIFT", 
         "Costos bancarios de $25 a $45 USD por giro internacional entrante, inviables para facturas recurrentes de $100 a $500 USD.", C_PURPLE_ACC, C_PURPLE_LT)
    ]

    for i, (title, desc, acc_color, bg_tint) in enumerate(probs):
        py = Inches(1.42) + i * Inches(1.42)
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, py, left_w, Inches(1.28))
        box.fill.solid()
        box.fill.fore_color.rgb = C_WHITE
        box.line.color.rgb = acc_color
        box.line.width = Pt(1.2)

        tb = s2.shapes.add_textbox(left_x + Inches(0.2), py + Inches(0.12), left_w - Inches(0.4), Inches(1.05))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(8.8)
        p_d.font.color.rgb = C_TEXT_MUTED
        p_d.space_before = Pt(3)

    # Banner inferior de propuesta Caleta
    sol_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, Inches(5.82), left_w, Inches(1.05))
    sol_box.fill.solid()
    sol_box.fill.fore_color.rgb = C_TEXT_DARK
    sol_box.line.color.rgb = C_TEAL_BRAND
    sol_box.line.width = Pt(1.5)

    tb_s = s2.shapes.add_textbox(left_x + Inches(0.2), Inches(5.9), left_w - Inches(0.4), Inches(0.9))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    tf_s.margin_left = tf_s.margin_right = tf_s.margin_top = 0

    p_st = tf_s.paragraphs[0]
    p_st.text = "PROPUESTA DE VALOR CALETA"
    p_st.font.name = FONT_FAMILY
    p_st.font.size = Pt(8.5)
    p_st.font.bold = True
    p_st.font.color.rgb = C_TEAL_BRAND

    p_sd = tf_s.add_paragraph()
    p_sd.text = "Cobra globalmente con tarjeta mediante enlace simple y recibe tus dólares directos en tu banco local en Ecuador (Comisión: 2.1% fija)."
    p_sd.font.name = FONT_FAMILY
    p_sd.font.size = Pt(9.5)
    p_sd.font.color.rgb = C_WHITE
    p_sd.space_before = Pt(2)

    # Columna derecha: Marco estético para Diagrama de Flujo de Fondos
    right_x = Inches(6.7)
    right_w = Inches(5.8)
    
    img_box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, Inches(1.42), right_w, Inches(5.45))
    img_box.fill.solid()
    img_box.fill.fore_color.rgb = C_WHITE
    img_box.line.color.rgb = C_BORDER
    img_box.line.width = Pt(1.2)

    # Cabecera de la tarjeta gráfica
    tb_gh = s2.shapes.add_textbox(right_x + Inches(0.25), Inches(1.55), right_w - Inches(0.5), Inches(0.35))
    tf_gh = tb_gh.text_frame
    tf_gh.margin_left = tf_gh.margin_top = 0
    p_gh = tf_gh.paragraphs[0]
    p_gh.text = "MAPEO CONCEPTUAL DEL FLUJO DE FONDOS Y LIQUIDACIÓN"
    p_gh.font.name = FONT_FAMILY
    p_gh.font.size = Pt(9)
    p_gh.font.bold = True
    p_gh.font.color.rgb = C_TEXT_DARK

    if os.path.exists(IMG_FONDOS):
        s2.shapes.add_picture(IMG_FONDOS, right_x + Inches(0.15), Inches(2.0), width=right_w - Inches(0.3))

    add_footer(s2, 2, 8)

    # =========================================================================
    # SLIDE 3: MARCO SCRUM & DINÁMICA DE REUNIONES (El Core de la Asignatura)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3, C_BG_LIGHT)
    add_header(s3, "02. Herramientas Ágiles para Reuniones", "Ceremonias Ágiles y Dinámica Colaborativa en el Sprint 1")

    ceremonies = [
        ("PLANNING", "Sprint Planning", "Planificación y Estimación", 
         [
             "• Sprint Goal consensuado por el equipo.",
             "• Estimación por Planning Poker (60h capacidad).",
             "• Desglose de 4 historias (PB-01 a PB-04)."
         ], 
         C_TEXT_DARK),
        ("DAILY SCRUM", "Daily Scrum", "Standup Diario de 15 Minutos", 
         [
             "• Sincronización diaria enfocada en 3 preguntas.",
             "• Detección temprana de bloqueos (cookies PKCE).",
             "• Cero reuniones extensas o desenfocadas."
         ], 
         C_CYAN_ACC),
        ("DOD", "Definition of Done", "Criterios de Calidad Aceptados", 
         [
             "• Código en main con Pull Request verificado.",
             "• Pipeline de CI en verde (TypeScript y ESLint).",
             "• Políticas RLS activas en PostgreSQL."
         ], 
         C_TEAL_BRAND),
        ("REVIEW & RETRO", "Review & Retro", "Inspección y Mejora Continua", 
         [
             "• Demostración navegable del software ante el PO.",
             "• Retrospectiva con técnica 'Mantener/Mejorar'.",
             "• Acuerdos claros de acción para el Sprint 2."
         ], 
         C_PURPLE_ACC)
    ]

    cw3 = Inches(2.78)
    gap3 = Inches(0.2)
    y3 = Inches(1.42)
    h3 = Inches(5.45)

    for i, (badge_text, title, subtitle, bullets, color_acc) in enumerate(ceremonies):
        cx = Inches(0.8) + i * (cw3 + gap3)
        
        # Tarjeta redondeada con marco coloreado integrado
        c_box = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, y3, cw3, h3)
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = C_WHITE
        c_box.line.color.rgb = color_acc
        c_box.line.width = Pt(1.5)

        # Pill badge superior armónico
        pill = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.2), y3 + Inches(0.2), cw3 - Inches(0.4), Inches(0.32))
        pill.fill.solid()
        pill.fill.fore_color.rgb = C_BG_LIGHT
        pill.line.color.rgb = color_acc
        pill.line.width = Pt(1)
        tf_pill = pill.text_frame
        tf_pill.margin_top = Inches(0.03)
        p_p = tf_pill.paragraphs[0]
        p_p.text = badge_text
        p_p.font.name = FONT_FAMILY
        p_p.font.size = Pt(8)
        p_p.font.bold = True
        p_p.font.color.rgb = color_acc
        p_p.alignment = PP_ALIGN.CENTER

        # Contenido textual con márgenes limpios
        tb = s3.shapes.add_textbox(cx + Inches(0.2), y3 + Inches(0.65), cw3 - Inches(0.4), h3 - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(12.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        p_sub = tf.add_paragraph()
        p_sub.text = subtitle
        p_sub.font.name = FONT_FAMILY
        p_sub.font.size = Pt(8.5)
        p_sub.font.color.rgb = color_acc
        p_sub.space_before = Pt(2)
        p_sub.space_after = Pt(14)

        for line in bullets:
            p_b = tf.add_paragraph()
            p_b.text = line
            p_b.font.name = FONT_FAMILY
            p_b.font.size = Pt(9.2)
            p_b.font.color.rgb = C_TEXT_MUTED
            p_b.space_before = Pt(6)

    add_footer(s3, 3, 8)

    # =========================================================================
    # SLIDE 4: PRODUCT BACKLOG DEL SPRINT 1 (Sprint Board / Kanban)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4, C_BG_LIGHT)
    add_header(s4, "03. Sprint Backlog & Entregables", "Historias de Usuario del Incremento: 100% Cumplidas")

    # Banner del Sprint Goal con diseño refinado
    sg_box = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.38), Inches(11.733), Inches(0.82))
    sg_box.fill.solid()
    sg_box.fill.fore_color.rgb = C_TEAL_LIGHT
    sg_box.line.color.rgb = C_TEAL_BRAND
    sg_box.line.width = Pt(1.5)

    tb_sg = s4.shapes.add_textbox(Inches(1.05), Inches(1.45), Inches(11.2), Inches(0.7))
    tf_sg = tb_sg.text_frame
    tf_sg.word_wrap = True
    tf_sg.margin_left = tf_sg.margin_right = tf_sg.margin_top = 0
    p_sg = tf_sg.paragraphs[0]
    p_sg.text = "SPRINT GOAL (OBJETIVO COMPROMETIDO Y ALCANZADO):"
    p_sg.font.name = FONT_FAMILY
    p_sg.font.size = Pt(8.5)
    p_sg.font.bold = True
    p_sg.font.color.rgb = C_TEAL_BRAND
    p_sg_sub = tf_sg.add_paragraph()
    p_sg_sub.text = "“Establecer la base arquitectónica cloud-native, diseño institucional y flujo de autenticación segura tipificada (Persona vs. Empresa).”"
    p_sg_sub.font.name = FONT_FAMILY
    p_sg_sub.font.size = Pt(10.5)
    p_sg_sub.font.bold = True
    p_sg_sub.font.color.rgb = C_TEXT_DARK

    stories = [
        ("PB-01: Landing Page Institucional", "Est. 12h | Real: 12h",
         "• Propuesta de valor contundente adaptada al mercado ecuatoriano.\n• Llamado a la acción directo, diseño mobile-first y navegación ágil.\n• Optimización de carga ultra rápida con Server Components de Next.js.", C_TEAL_BRAND),
        ("PB-02: Registro Tipificado de Usuarios", "Est. 16h | Real: 18h",
         "• Segmentación clara: Freelancer (Persona Natural) vs. Empresa (PYME).\n• Validación en tiempo real de correos, contraseñas y sanitización.\n• Inserción atómica en tabla `profiles` mediante trigger de PostgreSQL.", C_CYAN_ACC),
        ("PB-03: Inicio de Sesión Seguro (Auth SSR)", "Est. 18h | Real: 18h",
         "• Autenticación con cookies seguras PKCE (Server-Side Auth Supabase).\n• Middleware (`proxy.ts`) que bloquea acceso no autorizado a rutas privadas.\n• Manejo visual interactivo de errores y feedback de carga al usuario.", C_PURPLE_ACC),
        ("PB-04: Recuperación de Contraseña", "Est. 14h | Real: 12h",
         "• Formulario de solicitud de token de restablecimiento por correo.\n• Pantalla de cambio de clave protegida y redirección automática.\n• Auditoría de seguridad sin exposición de credenciales en cliente.", C_AMBER_ACC)
    ]

    gw = Inches(5.75)
    gh = Inches(2.15)
    coords = [
        (Inches(0.8), Inches(2.42)),
        (Inches(6.78), Inches(2.42)),
        (Inches(0.8), Inches(4.72)),
        (Inches(6.78), Inches(4.72))
    ]

    for i, (title, meta, bullets, color_bar) in enumerate(stories):
        x, y = coords[i]
        b_shape = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, gw, gh)
        b_shape.fill.solid()
        b_shape.fill.fore_color.rgb = C_WHITE
        b_shape.line.color.rgb = color_bar
        b_shape.line.width = Pt(1.2)

        # Badge verde "COMPLETADO"
        badge = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x + gw - Inches(1.4), y + Inches(0.14), Inches(1.25), Inches(0.28))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_GREEN_LT
        badge.line.color.rgb = C_GREEN_OK
        badge.line.width = Pt(1)
        tf_bg = badge.text_frame
        tf_bg.margin_top = Inches(0.02)
        p_bg = tf_bg.paragraphs[0]
        p_bg.text = "✓ COMPLETADO"
        p_bg.font.name = FONT_FAMILY
        p_bg.font.size = Pt(7.5)
        p_bg.font.bold = True
        p_bg.font.color.rgb = C_GREEN_OK
        p_bg.alignment = PP_ALIGN.CENTER

        tb = s4.shapes.add_textbox(x + Inches(0.22), y + Inches(0.15), gw - Inches(1.6), gh - Inches(0.25))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(11)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        p_m = tf.add_paragraph()
        p_m.text = meta
        p_m.font.name = FONT_FAMILY
        p_m.font.size = Pt(8.5)
        p_m.font.bold = True
        p_m.font.color.rgb = color_bar
        p_m.space_before = Pt(2)
        p_m.space_after = Pt(4)

        for line in bullets.split("\n"):
            p_b = tf.add_paragraph()
            p_b.text = line
            p_b.font.name = FONT_FAMILY
            p_b.font.size = Pt(8.5)
            p_b.font.color.rgb = C_TEXT_MUTED
            p_b.space_before = Pt(2)

    add_footer(s4, 4, 8)

    # =========================================================================
    # SLIDE 5: BURNDOWN CHART Y MÉTRICAS ÁGILES (Data-Driven)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5, C_BG_LIGHT)
    add_header(s5, "04. Métricas Ágiles & Velocidad", "Burndown Chart del Sprint 1: Esfuerzo Planificado vs. Real")

    # Contenedor Gráfico (Izquierda) - Marco limpio con cabecera
    bx_w = Inches(6.5)
    bx_h = Inches(5.45)
    b_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.42), bx_w, bx_h)
    b_card.fill.solid()
    b_card.fill.fore_color.rgb = C_WHITE
    b_card.line.color.rgb = C_BORDER
    b_card.line.width = Pt(1.2)

    tb_bh = s5.shapes.add_textbox(Inches(1.05), Inches(1.55), bx_w - Inches(0.5), Inches(0.35))
    tf_bh = tb_bh.text_frame
    tf_bh.margin_left = tf_bh.margin_top = 0
    p_bh = tf_bh.paragraphs[0]
    p_bh.text = "REGISTRO DIARIO DE ESFUERZO (LÍNEA IDEAL VS. LÍNEA REAL)"
    p_bh.font.name = FONT_FAMILY
    p_bh.font.size = Pt(9)
    p_bh.font.bold = True
    p_bh.font.color.rgb = C_TEXT_DARK

    if os.path.exists(IMG_BURNDOWN):
        s5.shapes.add_picture(IMG_BURNDOWN, Inches(0.95), Inches(1.95), width=bx_w - Inches(0.3))

    # Columna derecha: 3 Estadísticas KPI + Análisis Ágil
    rx = Inches(7.55)
    rw = Inches(4.98)

    kpis = [
        ("60 HORAS", "Capacidad Total", C_TEXT_DARK),
        ("18 HORAS", "Restantes Día 7", C_CYAN_ACC),
        ("100%", "Criterios DoD", C_GREEN_OK)
    ]

    kw = (rw - Inches(0.3)) / 3
    for i, (val, title, col) in enumerate(kpis):
        kx = rx + i * (kw + Inches(0.15))
        k_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, kx, Inches(1.42), kw, Inches(1.25))
        k_box.fill.solid()
        k_box.fill.fore_color.rgb = C_WHITE
        k_box.line.color.rgb = col
        k_box.line.width = Pt(1.2)

        tb_k = s5.shapes.add_textbox(kx + Inches(0.08), Inches(1.55), kw - Inches(0.16), Inches(1.0))
        tf_k = tb_k.text_frame
        tf_k.word_wrap = True
        tf_k.margin_left = tf_k.margin_right = tf_k.margin_top = 0
        
        p_val = tf_k.paragraphs[0]
        p_val.text = val
        p_val.font.name = FONT_FAMILY
        p_val.font.size = Pt(15.5)
        p_val.font.bold = True
        p_val.font.color.rgb = col
        p_val.alignment = PP_ALIGN.CENTER

        p_t = tf_k.add_paragraph()
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(7.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_MUTED
        p_t.alignment = PP_ALIGN.CENTER
        p_t.space_before = Pt(3)

    # Tarjeta de Análisis Ágil con marco integrado
    a_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(2.88), rw, Inches(3.99))
    a_card.fill.solid()
    a_card.fill.fore_color.rgb = C_WHITE
    a_card.line.color.rgb = C_TEAL_BRAND
    a_card.line.width = Pt(1.5)

    tb_a = s5.shapes.add_textbox(rx + Inches(0.25), Inches(3.08), rw - Inches(0.5), Inches(3.6))
    tf_a = tb_a.text_frame
    tf_a.word_wrap = True
    tf_a.margin_left = tf_a.margin_right = tf_a.margin_top = 0

    p_at = tf_a.paragraphs[0]
    p_at.text = "ANÁLISIS DE VELOCIDAD Y AUTOORGANIZACIÓN"
    p_at.font.name = FONT_FAMILY
    p_at.font.size = Pt(10.5)
    p_at.font.bold = True
    p_at.font.color.rgb = C_TEXT_DARK

    analisis_points = [
        ("• Comportamiento de la Curva:", "Los primeros 4 días mostraron una velocidad óptima paralela a la línea ideal de quemado."),
        ("• Bloqueo en Día 5 y 6:", "La investigación sobre cookies seguras PKCE en Server Components generó una meseta temporal."),
        ("• Capacidad de Autoorganización:", "El equipo resolvió el bloqueo en el Daily Scrum, acelerando en el Día 7 con 18h restantes."),
        ("• Conclusión:", "El incremento base se completó sin recortar alcance ni comprometer la calidad del código.")
    ]

    for title, desc in analisis_points:
        p_ap = tf_a.add_paragraph()
        p_ap.text = title
        p_ap.font.name = FONT_FAMILY
        p_ap.font.size = Pt(8.8)
        p_ap.font.bold = True
        p_ap.font.color.rgb = C_TEAL_BRAND
        p_ap.space_before = Pt(6)

        p_ad = tf_a.add_paragraph()
        p_ad.text = desc
        p_ad.font.name = FONT_FAMILY
        p_ad.font.size = Pt(8.2)
        p_ad.font.color.rgb = C_TEXT_MUTED
        p_ad.space_before = Pt(1)

    add_footer(s5, 5, 8)

    # =========================================================================
    # SLIDE 6: ARQUITECTURA DE SOFTWARE Y SEGURIDAD CLOUD-NATIVE
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6, C_BG_LIGHT)
    add_header(s6, "05. Arquitectura Técnica & Seguridad", "Arquitectura Desacoplada Cloud-Native y Seguridad por Capas")

    ax_w = Inches(6.0)
    ax_h = Inches(5.45)
    a_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.42), ax_w, ax_h)
    a_card.fill.solid()
    a_card.fill.fore_color.rgb = C_WHITE
    a_card.line.color.rgb = C_BORDER
    a_card.line.width = Pt(1.2)

    tb_ah = s6.shapes.add_textbox(Inches(1.05), Inches(1.55), ax_w - Inches(0.5), Inches(0.35))
    tf_ah = tb_ah.text_frame
    tf_ah.margin_left = tf_ah.margin_top = 0
    p_ah = tf_ah.paragraphs[0]
    p_ah.text = "DIAGRAMA DE ARQUITECTURA DESACOPLADA (NEXT.JS + SUPABASE)"
    p_ah.font.name = FONT_FAMILY
    p_ah.font.size = Pt(8.5)
    p_ah.font.bold = True
    p_ah.font.color.rgb = C_TEXT_DARK

    if os.path.exists(IMG_ARQ):
        s6.shapes.add_picture(IMG_ARQ, Inches(0.95), Inches(2.0), width=ax_w - Inches(0.3))

    rx6 = Inches(7.05)
    rw6 = Inches(5.48)

    tech_pillars = [
        ("⚡ Next.js 16 (App Router & Turbopack)", 
         "Arquitectura moderna basada en Server Components para renderizado ultrarrápido y reducción drástica del bundle en el cliente.", C_TEXT_DARK),
        ("🎨 Tailwind CSS v4 & Lucide Icons", 
         "Sistema de diseño moderno, limpio y responsive adaptado a las guías visuales de plataformas financieras de primer nivel.", C_CYAN_ACC),
        ("🔒 Supabase Auth SSR & Cookies PKCE", 
         "Autenticación segura en el servidor sin almacenar tokens sensibles en el LocalStorage, mitigando riesgos de XSS.", C_TEAL_BRAND),
        ("🛡️ PostgreSQL RLS (Row Level Security)", 
         "Políticas de aislamiento de datos a nivel de motor de base de datos: ningún usuario puede leer ni modificar perfiles ajenos.", C_PURPLE_ACC)
    ]

    for i, (title, desc, acc_col) in enumerate(tech_pillars):
        cy = Inches(1.42) + i * Inches(1.38)
        c_p = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx6, cy, rw6, Inches(1.25))
        c_p.fill.solid()
        c_p.fill.fore_color.rgb = C_WHITE
        c_p.line.color.rgb = acc_col
        c_p.line.width = Pt(1.2)

        tb = s6.shapes.add_textbox(rx6 + Inches(0.2), cy + Inches(0.14), rw6 - Inches(0.4), Inches(0.98))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = 0

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.name = FONT_FAMILY
        p_t.font.size = Pt(10.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_DARK

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.name = FONT_FAMILY
        p_d.font.size = Pt(8.5)
        p_d.font.color.rgb = C_TEXT_MUTED
        p_d.space_before = Pt(3)

    add_footer(s6, 6, 8)

    # =========================================================================
    # SLIDE 7: DEMOSTRACIÓN VISUAL DEL SOFTWARE (MOCKUP DE NAVEGADOR ESTÉTICO)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7, C_BG_LIGHT)
    add_header(s7, "06. Demostración del Software", "Evidencias Visuales del Incremento Base en Funcionamiento")

    demo_w = Inches(5.7)
    demo_h = Inches(5.45)

    # Mockup 1: Landing Page
    d1_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.42), demo_w, demo_h)
    d1_card.fill.solid()
    d1_card.fill.fore_color.rgb = C_WHITE
    d1_card.line.color.rgb = C_TEAL_BRAND
    d1_card.line.width = Pt(1.5)

    # Barra superior del navegador simulado
    top_nav1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.95), Inches(1.55), demo_w - Inches(0.3), Inches(0.42))
    top_nav1.fill.solid()
    top_nav1.fill.fore_color.rgb = C_BG_LIGHT
    top_nav1.line.color.rgb = C_BORDER
    top_nav1.line.width = Pt(1)

    # Puntos de ventana macOS (Rojo, Amarillo, Verde)
    dot_colors = [RGBColor(255, 95, 86), RGBColor(255, 189, 46), RGBColor(39, 201, 63)]
    for di, dot_c in enumerate(dot_colors):
        dot = s7.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.1) + di * Inches(0.18), Inches(1.68), Inches(0.12), Inches(0.12))
        dot.fill.solid()
        dot.fill.fore_color.rgb = dot_c
        dot.line.fill.background()

    # Barra de dirección URL simulada
    url_box1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.8), Inches(1.60), Inches(4.5), Inches(0.30))
    url_box1.fill.solid()
    url_box1.fill.fore_color.rgb = C_WHITE
    url_box1.line.color.rgb = C_BORDER
    url_box1.line.width = Pt(0.8)
    tf_u1 = url_box1.text_frame
    tf_u1.margin_top = Inches(0.02)
    p_u1 = tf_u1.paragraphs[0]
    p_u1.text = "🔒 https://caleta.ec  (Landing Page Institucional)"
    p_u1.font.name = FONT_FAMILY
    p_u1.font.size = Pt(7.5)
    p_u1.font.color.rgb = C_TEXT_MUTED

    # Imagen Landing
    if os.path.exists(IMG_LANDING):
        s7.shapes.add_picture(IMG_LANDING, Inches(0.95), Inches(2.10), width=demo_w - Inches(0.3))

    # Pie explicativo de la pantalla 1
    tb_exp1 = s7.shapes.add_textbox(Inches(1.0), Inches(6.20), demo_w - Inches(0.4), Inches(0.6))
    tf_exp1 = tb_exp1.text_frame
    tf_exp1.word_wrap = True
    tf_exp1.margin_left = tf_exp1.margin_top = 0
    p_e1 = tf_exp1.paragraphs[0]
    p_e1.text = "Propuesta de valor clara, badge regional dinámico y botón de conversión."
    p_e1.font.name = FONT_FAMILY
    p_e1.font.size = Pt(8.5)
    p_e1.font.color.rgb = C_TEXT_MUTED

    # Mockup 2: Registro Tipificado
    d2_card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.42), demo_w, demo_h)
    d2_card.fill.solid()
    d2_card.fill.fore_color.rgb = C_CYAN_ACC
    d2_card.line.color.rgb = C_CYAN_ACC
    d2_card.line.width = Pt(1.5)

    # Barra superior del navegador simulado 2
    top_nav2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), Inches(1.55), demo_w - Inches(0.3), Inches(0.42))
    top_nav2.fill.solid()
    top_nav2.fill.fore_color.rgb = C_BG_LIGHT
    top_nav2.line.color.rgb = C_BORDER
    top_nav2.line.width = Pt(1)

    for di, dot_c in enumerate(dot_colors):
        dot = s7.shapes.add_shape(MSO_SHAPE.OVAL, Inches(7.1) + di * Inches(0.18), Inches(1.68), Inches(0.12), Inches(0.12))
        dot.fill.solid()
        dot.fill.fore_color.rgb = dot_c
        dot.line.fill.background()

    url_box2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.60), Inches(4.5), Inches(0.30))
    url_box2.fill.solid()
    url_box2.fill.fore_color.rgb = C_WHITE
    url_box2.line.color.rgb = C_BORDER
    url_box2.line.width = Pt(0.8)
    tf_u2 = url_box2.text_frame
    tf_u2.margin_top = Inches(0.02)
    p_u2 = tf_u2.paragraphs[0]
    p_u2.text = "🔒 https://caleta.ec/registro  (Registro Tipificado)"
    p_u2.font.name = FONT_FAMILY
    p_u2.font.size = Pt(7.5)
    p_u2.font.color.rgb = C_TEXT_MUTED

    # Imagen Registro
    if os.path.exists(IMG_REGISTRO):
        s7.shapes.add_picture(IMG_REGISTRO, Inches(6.95), Inches(2.10), width=demo_w - Inches(0.3))

    # Pie explicativo de la pantalla 2
    tb_exp2 = s7.shapes.add_textbox(Inches(7.0), Inches(6.20), demo_w - Inches(0.4), Inches(0.6))
    tf_exp2 = tb_exp2.text_frame
    tf_exp2.word_wrap = True
    tf_exp2.margin_left = tf_exp2.margin_top = 0
    p_e2 = tf_exp2.paragraphs[0]
    p_e2.text = "Selector Freelancer vs. Empresa con inserción atómica en base de datos."
    p_e2.font.name = FONT_FAMILY
    p_e2.font.size = Pt(8.5)
    p_e2.font.color.rgb = C_TEXT_MUTED

    add_footer(s7, 7, 8)

    # =========================================================================
    # SLIDE 8: RETROSPECTIVA Y PRÓXIMOS PASOS (Cierre Keynote Oscuro #0B132B)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8, C_DARK_NAVY)

    bar10 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.1))
    bar10.fill.solid()
    bar10.fill.fore_color.rgb = C_TEAL_BRAND
    bar10.line.fill.background()

    add_header(s8, "07. Retrospectiva & Hoja de Ruta", "Lecciones del Sprint 1 y Próximo Incremento (Sprint 2)", dark_mode=True)

    w8 = Inches(5.7)
    h8 = Inches(4.75)
    
    # Tarjeta Izquierda: Retrospectiva con marco integrado coloreado
    card_retro = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.42), w8, h8)
    card_retro.fill.solid()
    card_retro.fill.fore_color.rgb = C_SLATE_CARD
    card_retro.line.color.rgb = C_TEAL_BRAND
    card_retro.line.width = Pt(1.5)

    pill_r = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(1.62), w8 - Inches(0.5), Inches(0.32))
    pill_r.fill.solid()
    pill_r.fill.fore_color.rgb = RGBColor(15, 23, 42)
    pill_r.line.color.rgb = C_TEAL_BRAND
    pill_r.line.width = Pt(1)
    tf_pr = pill_r.text_frame
    tf_pr.margin_top = Inches(0.03)
    p_pr = tf_pr.paragraphs[0]
    p_pr.text = "RETROSPECTIVA DE LA REUNIÓN ÁGIL"
    p_pr.font.name = FONT_FAMILY
    p_pr.font.size = Pt(8.5)
    p_pr.font.bold = True
    p_pr.font.color.rgb = C_TEAL_BRAND
    p_pr.alignment = PP_ALIGN.CENTER

    tb_r = s8.shapes.add_textbox(Inches(1.05), Inches(2.05), w8 - Inches(0.5), h8 - Inches(0.8))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    tf_r.margin_left = tf_r.margin_right = tf_r.margin_top = 0

    retro_points = [
        ("🌟 Lo que funcionó excelente:", 
         "• Integración fluida entre diseño UX y arquitectura backend.\n• Automatización del pipeline de CI (cero errores de compilación).\n• Standups diarios ágiles de 15 minutos con resolución inmediata.", C_TEAL_BRAND),
        ("💡 Oportunidad de mejora:", 
         "• Anticipar la curva de aprendizaje en dependencias nuevas (Supabase SSR) al estimar horas de investigación técnica.", C_AMBER_ACC),
        ("🎯 Compromiso para Sprint 2:", 
         "• Realizar pruebas de integración documental antes del merge final a producción.", C_CYAN_ACC)
    ]

    for title, text, color in retro_points:
        p_st = tf_r.add_paragraph()
        p_st.text = title
        p_st.font.name = FONT_FAMILY
        p_st.font.size = Pt(9.5)
        p_st.font.bold = True
        p_st.font.color.rgb = color
        p_st.space_before = Pt(8)
        p_st.space_after = Pt(2)

        for line in text.split("\n"):
            p_sl = tf_r.add_paragraph()
            p_sl.text = line
            p_sl.font.name = FONT_FAMILY
            p_sl.font.size = Pt(8.5)
            p_sl.font.color.rgb = RGBColor(203, 213, 225)
            p_sl.space_before = Pt(2)

    # Tarjeta Derecha: Roadmap Sprint 2
    card_next = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.42), w8, h8)
    card_next.fill.solid()
    card_next.fill.fore_color.rgb = C_SLATE_CARD
    card_next.line.color.rgb = C_CYAN_ACC
    card_next.line.width = Pt(1.5)

    pill_n = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.05), Inches(1.62), w8 - Inches(0.5), Inches(0.32))
    pill_n.fill.solid()
    pill_n.fill.fore_color.rgb = RGBColor(15, 23, 42)
    pill_n.line.color.rgb = C_CYAN_ACC
    pill_n.line.width = Pt(1)
    tf_pn = pill_n.text_frame
    tf_pn.margin_top = Inches(0.03)
    p_pn = tf_pn.paragraphs[0]
    p_pn.text = "ROADMAP DEL SPRINT 2 (26/OCT – 06/NOV)"
    p_pn.font.name = FONT_FAMILY
    p_pn.font.size = Pt(8.5)
    p_pn.font.bold = True
    p_pn.font.color.rgb = C_CYAN_ACC
    p_pn.alignment = PP_ALIGN.CENTER

    tb_n = s8.shapes.add_textbox(Inches(7.05), Inches(2.05), w8 - Inches(0.5), h8 - Inches(0.8))
    tf_n = tb_n.text_frame
    tf_n.word_wrap = True
    tf_n.margin_left = tf_n.margin_right = tf_n.margin_top = 0

    next_points = [
        ("PB-05: Verificación Documental KYC / KYB", 
         "Subida de cédula, RUC y comprobantes a Supabase Storage con encriptación y permisos restringidos.", C_CYAN_ACC),
        ("PB-06: Gestión de Cuentas Bancarias Locales", 
         "Módulo para registrar y validar cuentas de ahorros/corrientes de bancos ecuatorianos para recepción de fondos.", C_TEAL_BRAND),
        ("PB-07: Generador de Payment Links", 
         "Creación de enlaces de cobro con parámetros dinámicos de monto, descripción y fecha de expiración.", C_PURPLE_ACC),
        ("Espacio para Preguntas y Feedback", 
         "¡Muchas gracias por su atención! Abrimos el espacio para preguntas y observaciones de la clase.", C_WHITE)
    ]

    for title, desc, color in next_points:
        p_st = tf_n.add_paragraph()
        p_st.text = title
        p_st.font.name = FONT_FAMILY
        p_st.font.size = Pt(9.5)
        p_st.font.bold = True
        p_st.font.color.rgb = color
        p_st.space_before = Pt(8)
        p_st.space_after = Pt(2)

        p_sl = tf_n.add_paragraph()
        p_sl.text = desc
        p_sl.font.name = FONT_FAMILY
        p_sl.font.size = Pt(8.5)
        p_sl.font.color.rgb = RGBColor(203, 213, 225)

    # Banner inferior de cierre
    cierre_box = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.35), Inches(11.733), Inches(0.55))
    cierre_box.fill.solid()
    cierre_box.fill.fore_color.rgb = RGBColor(20, 31, 56)
    cierre_box.line.color.rgb = C_TEAL_BRAND
    cierre_box.line.width = Pt(1)

    tb_ci = s8.shapes.add_textbox(Inches(1.0), Inches(6.42), Inches(11.333), Inches(0.4))
    tf_ci = tb_ci.text_frame
    tf_ci.margin_left = tf_ci.margin_right = tf_ci.margin_top = 0
    p_ci = tf_ci.paragraphs[0]
    p_ci.text = "“Caleta: Cobra globalmente. Recibe localmente.”  •  Fin de la Presentación del Sprint 1"
    p_ci.font.name = FONT_FAMILY
    p_ci.font.size = Pt(9.5)
    p_ci.font.bold = True
    p_ci.font.color.rgb = C_TEAL_BRAND
    p_ci.alignment = PP_ALIGN.CENTER

    add_footer(s8, 8, 8, dark_mode=True)

    # --- GUARDAR ARCHIVO PPTX ---
    pptx_path = os.path.join(ENTREGABLES_DIR, "Presentacion_Primer_Avance_Sprint_1.pptx")
    prs.save(pptx_path)
    print(f"Presentación PPTX generada exitosamente en: {pptx_path}")
    return pptx_path


if __name__ == "__main__":
    pptx_file = create_presentation()
    pdf_file = pptx_file.replace(".pptx", ".pdf")
    
    print("Iniciando conversión de PPTX a PDF mediante PowerPoint COM...")
    ps_cmd = f"""
    $ppt = New-Object -ComObject PowerPoint.Application
    $pres = $ppt.Presentations.Open("{pptx_file}", [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
    $pres.SaveAs("{pdf_file}", 32)
    $pres.Close()
    $ppt.Quit()
    """
    try:
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, text=True, check=True)
        print(f"PDF generado exitosamente en: {pdf_file}")
    except Exception as e:
        print(f"Advertencia al convertir vía PowerPoint COM: {e}")
