import fitz
import os

pdf_path = "FM-1-manual.pdf"
output_pdf_path = "FM-1-manual-RU.pdf"

doc = fitz.open(pdf_path)

# Найдем шрифт Arial для поддержки кириллицы
font_path = "C:/Windows/Fonts/arial.ttf"
font_bold_path = "C:/Windows/Fonts/arialbd.ttf"

for page_num in range(len(doc)):
    page = doc[page_num]
    
    # Извлечем текстовые блоки с позициями
    blocks = page.get_text("blocks")
    
    # Для каждого блока заменим англоязычный текст на русские эквиваленты
    # Поскольку простое наложение текста поверх может привести к наложению, 
    # сначала закрасим старый текст белыми прямоугольниками (или удалим его)
    for b in blocks:
        # b = (x0, y0, x1, y1, text, block_no, block_type)
        if b[6] == 0:  # текстовый блок
            rect = fitz.Rect(b[:4])
            # Закрасим белым цветом оригинал текста
            page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))

doc.save("test_blank.pdf")
print("Blank test done.")
