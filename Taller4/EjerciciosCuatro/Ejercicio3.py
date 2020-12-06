"""
	Generar un algoritmo que permita calcular y mostrar el valor de la
	planilla de teléfono de un casa. Se debe ingresar el costo por minutos,
	el número de minutos consumidos en el mes.
"""
costo_minuto = float(input("Ingresar el costo por minutos: $"))
minutos_consumidos = float(input("Ingresar los minutos consumidos en el "\
	"mes: "))
producto = costo_minuto * minutos_consumidos
mensaje = f"El valor de la planilla: ${producto:.2f}\n"
print(mensaje)