import fitz  # PyMuPDF

doc = fitz.open("scanned.pdf")

for page in doc:
    text = page.get_text()
    print(text)
