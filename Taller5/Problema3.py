"""
	Elaborar una solución que permita leer los datos de un automóvil (marca,
	origen y costo) imprima el impuesto por pagar y el precio de venta
	(incluido el impuesto). Si el origen es Alemania el impuesto es 20%, si es
	de Japón el impuesto es 30%, si es de Italia, 15%, y si es de USA, 8%
"""
marca = input("Ingresar la marca del automóvil: ")
origen = input("Ingresar país de origen del automóvil:\n-Alemania\t-Japon\n"\
	"-Italia\t\t-USA: ")
costo = float(input("Ingresar costo del automóvil: "))
if (origen == "Alemania"):
	impuesto = costo * 0.2  #20%
	porcentajeImpuesto = "20%"
	total = costo + impuesto
if (origen == "Japon"):
	impuesto = costo * 0.3  #30%
	porcentajeImpuesto = "30%"
	total = costo + impuesto
if (origen == "Italia"):
	impuesto = costo * 0.15  #15%
	porcentajeImpuesto = "15%"
	total = costo + impuesto
if (origen == "USA"):
	impuesto = costo * 0.08  #8%
	porcentajeImpuesto = "8%"
	total = costo + impuesto
mensaje = f"Marca de automovil: {marca}\nPaís de origen: {origen}\n"\
f"Costo inicial ${costo:.2f}\nImpuesto por pagar {porcentajeImpuesto}: "\
f"${impuesto:.2f}\nPrecio de venta: ${total:.2f}\n"
print(mensaje)