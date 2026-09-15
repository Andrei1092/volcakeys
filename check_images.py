import fitz

pdf_path = "FM-1-manual.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    for img in page.get_images():
        print(f"Page {page_num+1} has image: {img[0]}")
