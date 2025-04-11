import re
from PyPDF2 import PdfReader
from tkinter import Tk, Button, Label, filedialog, messagebox
import os
from datetime import datetime
import json

with open("DIM2.pdf", "rb") as pdffileobj:
    pdfreader = PdfReader(pdffileobj)
    full_text = ""
    for page in pdfreader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

pattern = r'([A-Z](?:\d+(?:\.\d+)*)\.)\s*([\s\S]*?)(?=(?:[A-Z](?:\d+(?:\.\d+)*)\.)|$)'
matches = re.findall(pattern, full_text, re.DOTALL)

 
campos = []
for id_actual, bloque in matches:
    bloque = bloque.strip()
    if '\n' in bloque:
        titulo, valor = bloque.split('\n', 1)
    else:
        titulo, valor = bloque, ""
    campos.append({
        'id': id_actual.strip(),
        'titulo': titulo.strip(),
        'valor': valor.strip()
    })

 
with open("campos.txt", "w", encoding="utf-8") as salida:
    for c in campos:
        # Formato: A5.  Título: ...  =>  Valor: ...
        salida.write(f"{c['id']}  Título: {c['titulo']}  =>  Valor: {c['valor']}\n")

print(f"Exportados {len(campos)} campos a 'campos.txt'")


# def cargar_json():
#     ruta = filedialog.askopenfilename(title="Selecciona un archivo JSON", filetypes=[("Archivos JSON", "*.json")])
#     if ruta:
#         with open(ruta, 'r', encoding='utf-8-sig') as f:
#             datos = json.load(f)
      
       
# # Interfaz
# ventana = Tk()
# ventana.title("Procesador de PDF a Excel")
# ventana.geometry("400x400")

# Label(ventana, text="Conversor DIM ➜ Excel (VLSC)", font=("Arial", 14)).pack(pady=20)
# Button(ventana, text="Cargar y Procesar PDF", command=cargar_json, width=30, height=2).pack()

# ventana.mainloop()
