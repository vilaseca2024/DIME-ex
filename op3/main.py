import sys
import Split
from subprocess import call
from PyPDF2 import PdfReader  

if len(sys.argv) < 2:
    print("Error\nFormato correcto:\n\tpython main.py archivo.pdf")
else:
    filename = sys.argv[1]
    directory = "splitted/" + filename

    # Llama a la función split del módulo Split
    Split.split(directory, filename)

    # Abrimos el PDF original para saber cuántas páginas tiene
    with open(filename, 'rb') as pdfFileObj:
        pdfReader = PdfReader(pdfFileObj)
        total_pages = len(pdfReader.pages)

        for i in range(total_pages):
            splitted_file_name = f"{directory}/{i}"
            call(["pdftotext", splitted_file_name + ".pdf"])
         
            with open(splitted_file_name + ".txt", "r", encoding="utf-8") as f:
                print(f"\n--- Página {i+1} ---")
                print(f.read())
