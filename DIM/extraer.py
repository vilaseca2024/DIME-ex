import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext("image_1.png", detail=0)
print(result)