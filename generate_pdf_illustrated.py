import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

font_path = "C:/Windows/Fonts/arial.ttf"
pdfmetrics.registerFont(TTFont('Arial', font_path))
pdfmetrics.registerFont(TTFont('Arial-Bold', "C:/Windows/Fonts/arialbd.ttf"))

pdf_filename = "FM-1_Synthesizer_Manual_RU_Illustrated.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'RuTitle', parent=styles['Heading1'],
    fontName='Arial-Bold', fontSize=15, leading=18, spaceAfter=6, textColor=colors.HexColor('#111111')
)
subtitle_style = ParagraphStyle(
    'RuSubtitle', parent=styles['Heading2'],
    fontName='Arial-Bold', fontSize=11, leading=14, spaceBefore=5, spaceAfter=2, textColor=colors.HexColor('#1f4e79')
)
body_style = ParagraphStyle(
    'RuBody', parent=styles['Normal'],
    fontName='Arial', fontSize=8, leading=10.5, spaceAfter=2, textColor=colors.HexColor('#222222')
)
bullet_style = ParagraphStyle(
    'RuBullet', parent=styles['Normal'],
    fontName='Arial', fontSize=7.5, leading=10, leftIndent=8, spaceAfter=2, textColor=colors.HexColor('#333333')
)

story = [
    Paragraph("Интерактивное руководство по синтезатору FM-1 (схематичное описание панели и элементов)", title_style),
    Spacer(1, 4)
]

left_panel_data = [
    [Paragraph("<b>➀ MASTER (Потенциометр)</b><br/>• Управляет общим уровнем громкости аудиовыхода.<br/>• Поворот по часовой стрелке — увеличение громкости, против часовой — уменьшение.", body_style),
     Paragraph("<b>➁ SELECT (Энкодер)</b><br/>• Переключает страницы параметров в текущем режиме.<br/>• Поворот по часовой — Страница 2, против часовой — Страница 1.<br/>• В режиме FX прокручивает 6 слотов эффектов.", body_style)],
    [Paragraph("<b>➂ PRESETS (Энкодер)</b><br/>• Прокрутка 128 пресетов (001–128).<br/>• Циклический выбор: после 128 идет 001 и наоборот.<br/>• Мгновенно загружает пресет, показывая всплывающее окно со списком и названием.", body_style),
     Paragraph("<b>➃ ALGORITHM (Энкодер)</b><br/>• Выбор алгоритма FM-синтеза (01–32).<br/>• Показывает схему маршрутизации операторов.<br/>• С зажатой кнопкой OCT−/OCT+ используется для транспонирования (от -12 до +12 полутонов).", body_style)]
]

t1 = Table(left_panel_data, colWidths=[270, 270])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8f9fa')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))

story.append(Paragraph("1. Левая панель — Основные элементы управления", subtitle_style))
story.append(t1)
story.append(Spacer(1, 4))

center_data = [
    [Paragraph("<b>2. Центральный 1.54\" TFT-дисплей</b><br/>• <b>Верхняя строка:</b> Номер и название голоса (например, <i>032 BRASS 1</i>).<br/>• <b>Центральная область:</b> Параметры, волновые формы, сетки эффектов, схемы алгоритмов.<br/>• <b>Нижняя строка:</b> Название режима и номер страницы (например, <i>1/2 LFO</i>).<br/>• Показывает индикатор батареи и временные всплывающие окна.", body_style),
     Paragraph("<b>➄ OCT− / OCT+ (Кнопки октав)</b><br/>• Сдвигают клавиатуру вверх/вниз на 1 октаву (до ±3).<br/>• Светодиоды показывают смещение: мигают при ±1/±2, горят постоянно при ±3.<br/>• Одновременное нажатие сбрасывает октаву и транспонирование в 0.", body_style)]
]

t2 = Table(center_data, colWidths=[270, 270])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8f9fa')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))

story.append(Paragraph("2. Центральная зона и управление октавами", subtitle_style))
story.append(t2)
story.append(Spacer(1, 4))

right_data = [
    [Paragraph("<b>3.1 Ручки параметров (KNOB 1 – KNOB 4)</b><br/>• 4 энкодера, управляющих параметрами активного режима (отображаются в нижней строке дисплея).<br/>• В режиме FX настраивают фильтры, реверберацию, задержку, искажения, хорус и фазер.<br/>• В режиме ENV/LFO/Edit регулируют огибающие, форму волны, частоты, расстройку операторов и масштабирование.", body_style),
     Paragraph("<b>3.2 Функциональные кнопки (Верхний ряд)</b><br/>• <b>FX:</b> Сетка эффектов 3×2, выбор и перестановка.<br/>• <b>SEL:</b> Захват и перемещение эффектов в цепи.<br/>• <b>ENV:</b> Редактирование ADSR-огибающей.<br/>• <b>LFO:</b> Настройка низкочастотного модулятора.<br/>• <b>EDIT:</b> Глубокое редактирование операторов OP1–6.<br/>• <b>GLO:</b> Глобальные параметры синтеза и банков.", body_style)]
]

t3 = Table(right_data, colWidths=[270, 270])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8f9fa')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))

story.append(Paragraph("3. Правая панель — Ручки и верхний ряд кнопок", subtitle_style))
story.append(t3)
story.append(Spacer(1, 4))

bottom_data = [
    [Paragraph("<b>3.3 Функциональные кнопки (Нижний ряд)</b><br/>• <b>HOME:</b> Долгая пауза — вкл/выкл Bluetooth. Короткое нажатие — возврат на главный экран и осциллограф.<br/>• <b>SAVE:</b> Сохранение текущих пресетов и настроек во флеш-память устройства.<br/>• <b>ARP:</b> Активация арпеджиатора (режимы Up, Down, Inclusive, Exclusive, Random, Order, Repeat).<br/>• <b>SEQ:</b> 16-шаговый секвенсор с поддержкой записи, шагов, Chain и Swing.<br/>• <b>PLAY/STOP & REC:</b> Управление воспроизведением и записью последовательностей.", body_style),
     Paragraph("<b>4. Клавиатура и соединения (Нижняя панель)</b><br/>• <b>27 клавиш:</b> Силиконовая клавиатура с подсветкой для игры, ввода шагов или арпеджиатора.<br/>• <b>Интерфейсы сзади:</b><br/>  1. 3.5 мм аудиовыход (TRS для наушников/колонок).<br/>  2. 3.5 мм порт MIDI IN.<br/>  3. USB Type-C порт питания и данных.<br/>  4. Тумблер питания устройства.<br/>• <b>Питание:</b> Аккумулятор 2000 мАч (до 12 часов) или USB.", body_style)]
]

t4 = Table(bottom_data, colWidths=[270, 270])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8f9fa')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d1d5db')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e5e7eb')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
]))

story.append(Paragraph("4. Нижний ряд кнопок, клавиатура и задняя панель", subtitle_style))
story.append(t4)

doc.build(story)
print("Illustrated PDF generated successfully.")
