import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    for b in page.get_text("blocks"):
        try:
            txt = b[4].strip()
            if "MASTER" in txt or "SELECT" in txt:
                print(f"Page {page_num+1}: {txt[:50]}")
        except:
            pass
