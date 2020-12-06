"""
	Realizar un programa en java que permita presentar un mensaje de: 
	acceso correcto, si el valor ingresado para la variable ciudad tiene el
	valor diferente de Loja; caso contrario, presentar un mensaje de acceso
	incorrecto
"""
ciudad = input("Ingrese la ciudad: ")
if (not ciudad == "Loja"):
	mensaje = "\nacceso correcto"
else:
	mensaje = "\nacceso incorrecto"
print(mensaje)