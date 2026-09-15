import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

font_path = "C:/Windows/Fonts/arial.ttf"
pdfmetrics.registerFont(TTFont('Arial', font_path))
pdfmetrics.registerFont(TTFont('Arial-Bold', "C:/Windows/Fonts/arialbd.ttf"))

pdf_filename = "FM-1-manual-RU-Illustrated.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'RuTitle', parent=styles['Heading1'],
    fontName='Arial-Bold', fontSize=16, leading=20, spaceAfter=10, textColor=colors.HexColor('#111111')
)
subtitle_style = ParagraphStyle(
    'RuSubtitle', parent=styles['Heading2'],
    fontName='Arial-Bold', fontSize=12, leading=15, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor('#1f4e79')
)
body_style = ParagraphStyle(
    'RuBody', parent=styles['Normal'],
    fontName='Arial', fontSize=9, leading=12, spaceAfter=4, textColor=colors.HexColor('#222222')
)

story = []

story.append(Paragraph("Синтезатор FM-1 — Подробное руководство пользователя", title_style))
story.append(Spacer(1, 10))

# Добавим сгенерированные изображения страниц с текстом перевода рядом или под ними
# Или соберем красивый иллюстрированный PDF на основе рендеров страниц и русскоязычного перевода

for i in range(1, 17):
    img_path = f"page_{i}.png"
    if os.path.exists(img_path):
        story.append(Paragraph(f"Страница {i}", subtitle_style))
        story.append(Image(img_path, width=450, height=600))
        story.append(PageBreak())

doc.build(story)
print("Illustrated translated PDF created.")
