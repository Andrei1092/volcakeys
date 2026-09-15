import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    drawings = page.get_drawings()
    print(f"Page {page_num+1}: {len(drawings)} drawing objects/vectors")
