"""
	Generar un programa que permita ingresar un nombre de una ciudad;
	Los nombres de las ciudades permitidas son las que empiezan con vocal.
	Si la ciudad es permitida presentar un mensaje:
	Nombre con inicial O de otavalo
	Si la ciudad no es permitida presentar un mensaje:
	opción incorrecta; ninguna de las anteriores
"""
nombre = input("Ingrese el nombre de una ciudad del Ecuador: ")
inicial = nombre[0]
if ((inicial == "a") or (inicial == "A")):
	mensajeFinal = f"Nombre con inicial {inicial} de {nombre}\n"
elif ((inicial == "e") or (inicial == "E")):
	mensajeFinal = f"Nombre con inicial {inicial} de {nombre}\n"
elif ((inicial == "i") or (inicial == "I")):
	mensajeFinal = f"Nombre con inicial {inicial} de {nombre}\n"
elif ((inicial == "o") or (inicial == "O")):
	mensajeFinal = f"Nombre con inicial {inicial} de {nombre}\n"
elif ((inicial == "u") or (inicial == "U")):
	mensajeFinal = f"Nombre con inicial {inicial} de {nombre}\n"
else:
	mensajeFinal = "Opción incorrecta; ninguna de las anteriores"
print(mensajeFinal)