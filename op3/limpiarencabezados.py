import fitz 
archivo_pdf = "DIM2.pdf"
doc = fitz.open(archivo_pdf)
zona_encabezado = fitz.Rect(0, 0, doc[0].rect.width, 60)
for pagina in doc:
    pagina.add_redact_annot(zona_encabezado, fill=(1, 1, 1))
    pagina.apply_redactions()
    pagina.insert_text(
        point=(zona_encabezado.x0 + 10, zona_encabezado.y0 + 15),  # posición ajustada
        text="Nueva pagina ojo",
        fontsize=10,
        fontname="helv",
        fill=(0, 0, 0),  # color negro
    )

