"""
	Se utiliza un ciclo repetitivo para ingresa calificaciones por teclado
	y para salir se debe digitar si para que el valor bandera se convierta
	en Falso y se termine el ciclo
	En pantalla se debe presentar un reporte como el siguiente

	Listado de notas
	10.00
	9.56
	Promedio: 9.78
"""
cadenaFinal = ""
bandera = True
contador = 0
promedio = 0
sumaNotas = 0
while (bandera):
	nota = float(input("Ingrese calificaciónes: "))
	cadenaFinal = f"{cadenaFinal}{nota:.2f}\n"
	sumaNotas = sumaNotas + nota
	salida = input("Ingrese (si) si desea salir del ciclo: ")
	salida = salida.lower()
	contador = contador + 1
	if (salida == "si"):
		bandera = False
promedio = sumaNotas / contador
cadenaFinal = f"Listado de Notas\n{cadenaFinal}Promedio: {promedio:.2f}\n"
print(cadenaFinal)