import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    if "1. Left Panel" in text:
        print(f"Found on page {page_num+1}")
        for b in page.get_text("blocks"):
            try:
                print(b[4].strip())
            except:
                pass
        break
