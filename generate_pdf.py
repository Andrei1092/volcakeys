import os
import pymupdf
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Откроем исходный PDF через PyMuPDF (fitz) и извлечем картинку передней панели (например, первую страницу как картинку)
doc_src = pymupdf.open() # у нас нет оригинала в папке, но мы можем отрендерить страницу или нарисовать схему, либо если оригинал был передан в чате — но в окружении файла самого исходного PDF нет, только скриншоты в виде текста/входов.
# Сделаем красивый компактный PDF с кириллицей и аккуратными отступами.

font_path = "C:/Windows/Fonts/arial.ttf"
pdfmetrics.registerFont(TTFont('Arial', font_path))
pdfmetrics.registerFont(TTFont('Arial-Bold', "C:/Windows/Fonts/arialbd.ttf"))

pdf_filename = "FM-1_Synthesizer_Manual_RU_Clean.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'RuTitle',
    parent=styles['Heading1'],
    fontName='Arial-Bold',
    fontSize=16,
    leading=20,
    spaceAfter=8,
    textColor=colors.HexColor('#1a1a1a')
)

subtitle_style = ParagraphStyle(
    'RuSubtitle',
    parent=styles['Heading2'],
    fontName='Arial-Bold',
    fontSize=11,
    leading=14,
    spaceBefore=6,
    spaceAfter=3,
    textColor=colors.HexColor('#2c3e50')
)

body_style = ParagraphStyle(
    'RuBody',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=8,
    leading=10.5,
    spaceAfter=2,
    textColor=colors.HexColor('#222222')
)

code_style = ParagraphStyle(
    'RuCode',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=7.5,
    leading=9.5,
    leftIndent=8,
    spaceAfter=2,
    textColor=colors.HexColor('#0044aa')
)

story = []

story.append(Paragraph("Подробное руководство пользователя — Синтезатор FM-1 (На русском языке)", title_style))
story.append(Spacer(1, 4))

sections = [
    ("1. Левая панель — Основные элементы управления", [
        "➀ MASTER (Потенциометр): Управляет основным уровнем громкости аудиовыхода (по часовой стрелке — громче, против часовой — тише).",
        "➁ SELECT (Энкодер): Переключает страницы параметров в текущем режиме (2 страницы). Поворот по часовой — Страница 2, против часовой — Страница 1. В режиме FX прокручивает 6 слотов эффектов.",
        "➂ PRESETS (Энкодер): Прокрутка 128 пресетов (001–128) с циклическим переходом. Каждый поворот мгновенно загружает пресет, отображая всплывающее окно со списком и названием.",
        "➃ ALGORITHM (Энкодер): Выбор алгоритма FM-синтеза (01–32) в обычном режиме. При зажатой кнопке OCT− / OCT+ регулирует транспонирование (от -12 до +12 полутонов)."
    ]),
    ("2. Центральный дисплей — 1.54\" TFT-экран", [
        "Дисплей разделен на три зоны: верхняя строка (номер и имя голоса), центральная область (параметры, волны, сетки эффектов) и нижняя строка (режим и страница). Отображает иконку батареи и всплывающие окна (громкость, пресеты, алгоритмы, октавы, предупреждения LOW BATTERY)."
    ]),
    ("3. Правая панель — Ручки параметров и функциональные кнопки", [
        "3.1 KNOB 1 – KNOB 4 (Энкодеры параметров): Функции зависят от текущего режима.",
        "• Режим FX (Эффекты): Управление фильтром, реверберацией, задержкой, искажением, хорусом и фазером.",
        "• Режим ENV (Огибающая): Attack, Decay, Sustain, Release (0–100%).",
        "• Режим LFO: Wave, Speed, PMD, AMD, Delay, Pitch Sens, Lfo Sync, Osc Sync.",
        "• Режим Edit (Операторы OP1–6): Настройка параметров, тунинга, огибающих, чувствительности.",
        "• Режим Globe (Система): MIDI-каналы, сброс патчей, глобальная скорость,滑音 (Glide).",
        "• Режим ARP (Арпеджиатор): Режимы, октавы, скорость, темп, gate, swing, latch.",
        "• Режим SEQ (Секвенсор): 16 шагов, паттерны, цепи, темп, гейт, свинг, транспонирование.",
        "3.2 Функциональные кнопки (Верхний ряд): FX, SEL, ENV, LFO, EDIT, GLO.",
        "3.3 Функциональные кнопки (Нижний ряд): HOME (Bluetooth / Главный экран), SAVE (Сохранение), ARP, SEQ, PLAY/STOP, REC."
    ]),
    ("4. Нижняя панель — Клавиатура и комбинированные функции", [
        "4.1 Клавиши пианино (27 клавиш): Стандартные клавиши для воспроизведения нот, ввода в арпеджиатор или шагов секвенсора.",
        "4.2 Комбинированные функциональные кнопки: В режиме Edit позволяют выбирать операторы (OP1–OP6), огибающую питча (PIT), глобальные параметры (GLO) и переключать режимы MONO / POLY."
    ]),
    ("5. MIDI Connectivity (Подключение MIDI)", [
        "Поддерживает одновременную работу трех интерфейсов: USB MIDI, BLE MIDI (беспроводное), 3.5 MIDI IN (традиционное). Принимает: Note On/Off, Pitch Bend, Control Change (CC), Program Change (PC), SysEx (дампы голосов Yamaha DX7)."
    ]),
    ("6. Батарея и питание", [
        "Отображение уровня заряда в углу экрана, полноэкранный варнинг LOW BATTERY при разряде. Встроенный динамик (отключается при подключении наушников)."
    ]),
    ("7. Интерфейсы на задней панели", [
        "1. 3.5 мм аудиовыход (рекомендуется TRS). 2. MIDI-вход (через переходник). 3. USB Type-C порт. 4. Тумблер питания."
    ]),
    ("8. Технические характеристики", [
        "Размеры: 161.5 x 96.5 x 28.6 мм | Вес: 251 г | Клавиатура: 27-кнопочная силиконовая",
        "Регуляторы: 1 ручка громкости (300°), 7 контроллеров (360°)",
        "Автономность: 12 часов | Питание: Аккумулятор 2000 мАч 3.7V (DTP704060) или USB"
    ])
]

for title, paragraphs in sections:
    story.append(Paragraph(title, subtitle_style))
    for p in paragraphs:
        if p.startswith("•") or p.startswith("1.") or p.startswith("2.") or p.startswith("3.") or p.startswith("4.") or p.startswith("5.") or p.startswith("6.") or p.startswith("7.") or p.startswith("8."):
            story.append(Paragraph(p, code_style))
        else:
            story.append(Paragraph(p, body_style))
    story.append(Spacer(1, 2))

doc.build(story)
print("Clean PDF generated successfully.")
