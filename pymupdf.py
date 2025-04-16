import fitz  # PyMuPDF

doc = fitz.open("scanned.pdf")

for page in doc:
    text = page.get_text()
    print(text)



# J. Información adicional del Ítem
# OI 23000649
# Liquidación total de tributos, exoneraciones, suspensiones u otros cargos (Expresado en bolivianos)
# Tipo Detalle Base imponible Alícuota Liq. de Tributos Exoneraciones Suspensiones Tributos Determ.
# GA GRAVAMEN ARANCELARIO 6366 10.0 637 0 0 637
# IVA IMPUESTO AL VALOR AGREGADO 7003 14.94 1046 0 0 1046

# En el caso de la J. sacame 3 objetos en este caso:	
# 	id: J.
# 	titulo: Información adicional del Ítem
# 	valor: OI 23001116

# 	id: J.IVA
# 	titulo: IVA
# 	valor: 1046

# 	id: J.GA
# 	titulo: GA
# 	valor: 637

# Es decir el ultimo valor que me dan aca para cada uno debe ser el valor
# GA GRAVAMEN ARANCELARIO 6366 10.0 637 0 0 637
# IVA IMPUESTO AL VALOR AGREGADO 7003 14.94 1046 0 0 1046
# ----------------------------------------------------
# G. Observaciones generales de la declaración
# Ninguna
# Liquidación total de tributos, exoneraciones, suspensiones u otros cargos ( Expresado en bolivianos )
# Tipo Detalle Liquidación de tributos Exoneraciones Suspensiones Tributos determinados
# GAGRAVAMEN ARANCELARIO 64403 0 0 64403
# IVAIMPUESTO AL VALOR AGREGADO 145852 0 0 145852
# Sub totales 210255 0 0 210255
# Total tributos a pagar 210255

# En el caso de la G. sacame 4 objetos en este caso:

# 	id: G.
# 	titulo: Observaciones generales de la declaración
# 	valor: Ninguna

# 	id: G.IVA
# 	titulo: IVA
# 	valor: 145852

# 	id: G.GA
# 	titulo: GA
# 	valor: 64403

# 	id: G.TOTAL
# 	titulo: Total tributos a pagar
# 	valor: 210255



# EXISTEN LOS SIGUIENTES ERRORES QUE PEUDES REVISAR

# E.  Título: Información y valores totales de la factura Factura 1 de 1  =>  Valor: 
# E1.1  Título: Categoría  =>  Valor: -
# E1.2  Título: Condición del proveedor  =>  Valor: 
# E1.01  Título: - FABRICANTE  =>  Valor: 
# E2.  Título: País de adquisición  =>  Valor: US - ESTADOS UNIDOS

# REVISA el E1.01 esta mal no existe deberia ser asi:
# E.  Título: Información y valores totales de la factura Factura 1 de 1  =>  Valor: 
# E1.  Título: Datos del Proveedor => Valor: COVORO MINING SOLUTIONS, LLC, FITE ROAD, 2571, , MEMPHIS - TENNESSEE, ESTADOS UNIDOS,
# (1)9013537184, james.stockbridge@draslovka.com
# E1.1  Título: Categoría  =>  Valor: -
# E1.2  Título: Condición del proveedor  =>  Valor: 01 - FABRICANTE
# E2.  Título: País de adquisición  =>  Valor: US - ESTADOS UNIDOS

# para el caso de B1 y B2 me reconoce asi:
# B.  Título: Operadores  =>  Valor: Datos Tipo de documento N° de documento Nombre/Razón social Categoría *Domicilio, Ciudad, País, Teléfono, Fax, Correo Electrónico
# B1.  Título: Importador: NIT 1020415021 MINERA SAN CRISTOBAL  =>  Valor: 
# A.  Título: OEA TARIJA, 12, ZONA CENTRAL, POTOSÍ, POTOSI, BOLIVIA,  =>  Valor: 2153777, 2153777,
# B2.  Título: Declarante: NIT 1000899025 VILASECA  =>  Valor: 
# A.  Título: AGENCIA DESPACHANTE DE  =>  Valor: ADUANAOEA MERCADO, 1328, CENTRAL, LA PAZ, LA PAZ, BOLIVIA, 2202077, 2201860,
# pero deberia ser asi:
# B.  Título: Operadores  =>  Valor: Datos Tipo de documento N° de documento Nombre/Razón social Categoría *Domicilio, Ciudad, País, Teléfono, Fax, Correo Electrónico
# B1.  Título: Importador  =>  Valor: NIT 1020415021 MINERA SAN CRISTOBAL
# B2.  Título: Declarante  =>  Valor: NIT 1000899025 VILASECA
# ------------------------------------------------------------------------------

# para el F7 esta mal lo que reconosce: 
# F7  Título: Gastos Trans hasta el lugar de  =>  Valor: importación (USD) 19688.39

# deberia ser asi:
# F7  Título: Gastos Trans hasta el lugar de importación (USD) =>  Valor: 19688.39

# ---------------------------------------------------------------
# en el caso del F9 esta asi:
# F9  Título: Gastos de carga, descarga, manipuleo y  =>  Valor: otros gastos (USD) 10,975
# deberia ser asi:
# F9.  Título: Gastos de carga, descarga, manipuleo y otros gastos (USD) =>  Valor: 10,975

# ---------------------------------
# en el caso de E1.2 igual esta mal : 
# E1.2  Título: Condición del proveedor  =>  Valor: 
# E1.01  Título: - FABRICANTE  =>  Valor: 

# deberia ser :
# E1.2  Título: Condición del proveedor  =>   01 - FABRICANTE

# una forma de darte cuenta que esta mal es que va en orden alfabetico creciente no puede haber una incoherencia como saltarse de A1 al A11 es consecutivo A1,A2,A3,B1,B2,B2.1,B2.2 Y ASI SUCESIBAMENTE
# -----------------------------
# PARA EL CASO DE H8.9 esta asi:
# H8.8  Título: Composición  =>  Valor: CIANURO DE SODIO 98.97%, HIDROXIDO DE SODIO 0.42%, CARBONATO DE SODIO 0.39%, SODIO FORMADO 0.09%, AGUA 0.04%
# H8.9  Título: Forma de presentación  =>  Valor: 
# H8.20  Título:   =>  Valor: 
# H8.10  Título: Material  =>  Valor: -IBC C/U DE 1000 KG EN CONTENEDOR

# deberia ser 
# H8.8  Título: Composición  =>  Valor: CIANURO DE SODIO 98.97%, HIDROXIDO DE SODIO 0.42%, CARBONATO DE SODIO 0.39%, SODIO FORMADO 0.09%, AGUA 0.04%
# H8.9 Título: Forma de presentación  =>  Valor: 20 IBC C/U DE 1000 KG EN CONTENEDOR
# H8.10  Título: Material  =>  Valor: -

# AQUI TE PASO UN EJEMPLO DE COMOE STA BOTANDO EL CASO DE LAS H8 ES EL QUE DEBERIAN SER CONSECUTIVOS 14 SUBNIVELES TE LOS PASOS
# H8.1  Título: Nombre Mercancia  =>  Valor: COMUNES
# H8.2  Título: Especifique Nombre Mercancia  =>  Valor: PANEL CORROCERAMICO
# H8.3  Título: Marca comercial  =>  Valor: CORROSION ENGINEERING
# H8.4  Título: Tipo  =>  Valor: TIPO 8
# H8.5  Título: Clase  =>  Valor: -
# H8.6  Título: Modelo  =>  Valor: CL-1633-2
# H8.7  Título: Cuantitativo 1  =>  Valor: 
# H8.400  Título: MM X 284 MM  =>  Valor: 
# H8.8  Título: Composición  =>  Valor: W/(2) 3/4\" X 1-1/2\"L STUD
# S.  Título: W/3/8\"  =>  Valor: 
# R.  Título: PERIMETER & GRID WR  =>  Valor: 
# H8.9  Título: Forma de presentación  =>  Valor: 
# H8.45  Título: UNIDADES EN CAJA COMPARTIDA CON  =>  Valor: TUERCAS Y ARANDELAS
# H8.10  Título: Material  =>  Valor: CAUCHO NATURAL ANTIABRASIVO Y METAL COMUN
# H8.11  Título: Uso  =>  Valor: OTRO
# H8.11.  Título: 1 Especifique Uso  =>  Valor: USO EN MINERIA
# H8.12  Título: Otras características  =>  Valor: OI 23000829, W/2-3/4\"RBR ON 1/4\"PL
# T.  Título: W/  =>  Valor: 1-1/2\"S
# Q.  Título: X 1-3/4\"H \"VINO\" CUBE  =>  Valor: 
# H8.13  Título: Año modelo  =>  Valor: -
# H8.14  Título: Año fabricacion =>  Valor: -

# Y ASI DEBERIA SER EL RESULTADO CONSIDERA DE SUMA IMPORTANCIA PARA EVITAR MAS ERRORES EN EL H8.9 QUIERO QUE EL VALOR SEA SOLO EL NUMERO ENTERO QUE ESTA EN ESTE CASO 45
# H8.1  Título: Nombre Mercancia  =>  Valor: COMUNES
# H8.2  Título: Especifique Nombre Mercancia  =>  Valor: PANEL CORROCERAMICO
# H8.3  Título: Marca comercial  =>  Valor: CORROSION ENGINEERING
# H8.4  Título: Tipo  =>  Valor: TIPO 8
# H8.5  Título: Clase  =>  Valor: -
# H8.6  Título: Modelo  =>  Valor: CL-1633-2
# H8.7  Título: Cuantitativo 1  =>  Valor: 400 MM X 284 MM   
# H8.8  Título: Composición  =>  Valor: W/(2) 3/4\" X 1-1/2\"L STUDS. W/3/8\"A.R. PERIMETER & GRID WRK.
# H8.9  Título: Forma de presentación  =>  Valor: 45
# H8.10  Título: Material  =>  Valor: CAUCHO NATURAL ANTIABRASIVO Y METAL COMUN
# H8.11  Título: Uso  =>  Valor: OTRO
# H8.11.  Título: 1 Especifique Uso  =>  Valor: USO EN MINERIA
# H8.12  Título: Otras características  =>  Valor: OI 23000829, W/2-3/4\"RBR ON 1/4\"PLT. W/1-1/2\"SQ. X 1-3/4\"H \"VINO\" CUBES.
# H8.13  Título: Año modelo  =>  Valor: -
# H8.14  Título: Año fabricacion =>  Valor: -