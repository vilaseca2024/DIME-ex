import json
import pandas as pd
from tkinter import Tk, Button, Label, filedialog, messagebox
import os
from datetime import datetime


def extraer_datos_json(json_data):
    try:
        datos = json_data
        item = datos["datosMercancias"][0]
        trans = datos["datosTransacciones"][0]
        lugar = datos["datosGenerales"]["lugares"]
        doc = datos["datosGenerales"]["identificacionDeclaracion"]

        descripcion_items = item.get("descripcionMercanciaComercial", {}).get("descripcionMinimasMercancias", [])
        descripcion_comercial = ""
        for desc in descripcion_items:
            if "especifiqueNombreTxt" in desc:
                descripcion_comercial = desc["especifiqueNombreTxt"]
                break

        fila = {
            "Fecha Orden": lugar.get("fechaEmbarque", ""),
            "Tipo Documento": "OI",
            "Número De Documento": item.get("observaciones", "").split()[1] if "observaciones" in item else "",
            "Proveedor": "61527",
            "Nombre Proveedor": item.get("factura", {}).get("proveedor", {}).get("razonSocial", "").split(" ", 1)[-1],
            "Condiciones de Entrega": trans["detalleTransaccion"]["incoterms"]["condicionEntrega"].get("codigo", ""),
            "Instrucciones Envío 1": trans["detalleTransaccion"]["incoterms"].get("lugarEntrega", ""),
            "Instrucciones Envío 2": lugar["paisExportacion"].get("descripcion", ""),
            "Número de Linea": 1,
            "Descripción Comercial": descripcion_comercial,
            "Cantidad": item["identificacionMercanciaItem"].get("cantidadUnidadComercial", ""),
            "Unidad": item["identificacionMercanciaItem"]["unidadComercial"].get("descripcion", ""),
            "Valor FOB (USD)": float(item["informacionValoresTransaccionItem"].get("valorFOBItemUSD", 0)),
            "OTROS GASTOS HASTA CIF (USD)": 0,
            "VALOR  CIF (USD)": 139508.76,
            "GA (BOB)": 0,
            "IVA (BOB)": 145065,
            "IDHE (BOB)": 0,
            "Uso SIDUNEA (BOB)": 100,
            "TOTAL TRIBUTOS PAGADOS (BOB)": 145165,
            "ALMACENAJE ALBO (BOB)": 0,
            "OTROS GASTOS (...)": 0,
            "COMISION AGENCIA (BOB)": 3883.92
        }

        return fila

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar el JSON:\n{str(e)}")
        return None

def cargar_json():
    ruta = filedialog.askopenfilename(title="Selecciona un archivo JSON", filetypes=[("Archivos JSON", "*.json")])
    if ruta:
        with open(ruta, 'r', encoding='utf-8-sig') as f:

            datos = json.load(f)
        fila = extraer_datos_json(datos)
        if fila:
            df = pd.DataFrame([fila])
            fecha = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_archivo = f"reporte_generado_{fecha}.xlsx"
            df.to_excel(nombre_archivo, index=False)
            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")

# Interfaz
ventana = Tk()
ventana.title("Procesador de JSON a Excel")
ventana.geometry("400x200")

Label(ventana, text="Conversor JSON ➜ Excel (VLSC)", font=("Arial", 14)).pack(pady=20)
Button(ventana, text="Cargar y Procesar JSON", command=cargar_json, width=30, height=2).pack()

ventana.mainloop()
