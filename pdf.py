import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path("scanned.pdf", 600)
text_data = ''
text = pytesseract.image_to_string(pages[1])
text_data += text + '\n'
print(text_data)