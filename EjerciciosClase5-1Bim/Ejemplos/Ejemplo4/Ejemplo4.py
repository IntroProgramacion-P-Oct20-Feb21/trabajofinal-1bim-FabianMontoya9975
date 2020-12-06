"""
	Realizar un programa en java que permita presentar un mensaje de: 
	acceso correcto, si el valor ingresaso para la variable ciudad tiene el
	valor de Loja; caso contrario, presentar un mensaje de acceso incorrecto
"""
ciudad = input("Ingrese la ciudad: ")
ciudad = ciudad.lower()
if ((ciudad == "loja") or (ciudad == "machala")):
	mensaje = "\nAcceso correcto"
else:
	mensaje = "\nAcceso incorrecto"
print(mensaje)