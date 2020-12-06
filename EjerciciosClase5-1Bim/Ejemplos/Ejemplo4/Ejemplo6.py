"""
	Realizar un programa en java que permita presentar un mensaje de:
	acceso correcto, si el valor de la primera letra de la variable ciudad
	tiene el valor de "L"; caso contrario, presentar un mensaje de acceso
	incorrecto
"""
ciudad = input("Ingrese la ciudad: ")
inicial = ciudad[0]
if (inicial == "L"):
	mensaje = "\nacceso correcto"
else:
	mensaje = "\nacceso incorrecto"
print(mensaje)