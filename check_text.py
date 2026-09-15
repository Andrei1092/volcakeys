import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    text_instances = page.get_text("blocks")
    print(f"--- Page {page_num+1} ---")
    for i, t in enumerate(text_instances[:5]): # первые 5 блоков
        print(f"Block {i}: {t[4].strip()}")
    break
