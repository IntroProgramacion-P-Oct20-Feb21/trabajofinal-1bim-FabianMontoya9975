"""
	Generar un algoritmo que permita calcular y mostrar el valor a cancelar de
	una planilla de luz. Se debe ingresar el valor de costo por kilovatio/hora
	y el número de kilovatios consumidos en el mes. Si el usuario tiene edad
	mayor a 65 años, se debe descontrar el 10%.
"""
edad = int(input("Ingresar edad del usuario: "))
costo_kilovatio_hora = float(input("Ingresar el costo del kilovatio/hora: $"))
kilovatios = float(input("Ingresar el número de kilovatios consumidos en el "\
	"mes: "))
planilla = costo_kilovatio_hora * kilovatios
descuento = planilla * 0.1
planilla_descuento = planilla - descuento
if edad >=65:
	mensaje = f"El usuario es mayor a 65 años.\nEl valor de su planilla "\
	f"con el 10% de descuento es: ${planilla_descuento:.2f}\n"
else:
	mensaje = f"El valor de su planilla es: ${planilla:.2f}\n"
print(mensaje)