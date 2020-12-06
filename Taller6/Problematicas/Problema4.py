"""
	Realizar un programa en Java que permita ingresar 10 jugadores de
	baloncesto; por cada jugador se pide los datos: nombre del jugador,
	la cantidad de puntos que anotó en la temporada, la cantidad de faltas
	de la temporada. Generar el siguiente reporte:

	Jugador 1	100		10
	Jugador 2	200		25
	Jugador 3	99		33
	Jugador 4	80		41
	Jugador 5	60		50
"""
contador = 1
cadenaFinal = ""
while (contador <= 10):
	nombre = input("Ingresar el nombre del jugador: ")
	puntosAnotados = int(input("Ingrese los puntos anotados de la "\
		"temporada: "))
	cantidadFaltas = int(input("Ingrese la cantidad de faltas de la "\
		"temporada: "))
	cadenaFinal = f"{cadenaFinal}{nombre}\t{puntosAnotados}\t"\
	f"{cantidadFaltas}\n"
	contador = contador + 1
print(f"{cadenaFinal}\n")