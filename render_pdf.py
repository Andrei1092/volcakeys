import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

zoom = 2  # увеличение для лучшего качества
mat = fitz.Matrix(zoom, zoom)

for page_num in range(len(doc)):
    page = doc[page_num]
    pix = page.get_pixmap(matrix=mat)
    pix.save(f"page_{page_num+1}.png")

print("Rendered all pages to PNG images.")
