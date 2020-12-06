"""
	Se utiliza un ciclo repetitivo para ingresa calificaciones por teclado
	y para salir se debe digitar sun munero menor igual que 0(cero) para que
	el valor bandera se convierta en Falso y se termine el ciclo
	En pantalla se debe presentar un reporte como el siguiente

	Listado de notas
	9.00
	9.26
"""
cadenaFinal = ""
bandera = True
while (bandera):
	nota = float(input("Ingrese calificaciones: "))
	cadenaFinal = f"{cadenaFinal}{nota:.2f}\n"
	salida = int(input("Ingrese un número menor a 0(cero) si desea salir del"\
		" ciclo: "))
	if (salida <= 0):
		bandera = False
cadenaFinal = f"Listado de Notas\n{cadenaFinal}\n"
print(cadenaFinal)