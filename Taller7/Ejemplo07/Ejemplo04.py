"""
	Generar una solución que permita ingresar jugadores de fútbol; por cada
	jugador se debe solicitar:
	-	Nombre el jugador
	- 	Posición en el campo de juego
	- 	Edad
	- 	Estatura

	El ciclo de ingreso de información deberá terminar cuando el usuario lo
	decida.
	Se debe imprimer el siguiente reporte (usar una cadena de acumulación):
	> Listado de Jugadores
	1. Alexander Dominguez -Arquero-, edad 32, estatura 1.95
	2. Xavier Arreaga -Defensa-, edad 24, estatura 1.85
	3. Moisés Caicedo -Mediocentro-, edad 19, estatura 1.88
	4. Ángel Mena -Delantero-, edad 32, estatura 1.75
	5. Michael Estrada -Delantero-, edad 27, estatura 1.93
	Promedio de edades:  26.8
	Promedio de estaturas: 1.87
"""
cadenaReporte = ""
bandera = True
sumaEdades = 0
sumaEstaturas = 0
contadorIteraciones = 0
cadenaReporte = f"{cadenaReporte}Listado de Jugadores\n"
while (bandera):
	nombreJugador = input("Ingrese el nombre del Jugador: ")
	posicionCampo = input("Ingrese la posición en el campo: ")
	edad = int(input("Ingrese la edad del Jugador: "))
	estatura = float(input("Ingrese la estatura del jugador: "))
	sumaEdades = sumaEdades + edad
	sumaEstaturas = sumaEstaturas + estatura
	contadorIteraciones = contadorIteraciones + 1
	cadenaReporte = f"{cadenaReporte}{contadorIteraciones}.) {nombreJugador}"\
	f" -{posicionCampo}-, edad {edad}, estatura {estatura:.2f}\n"
	salir = input("Desea salir del ciclo; digite: si : ")
	salir = salir.lower()
	if (salir == "si"):
		bandera = False
promedioEdad = sumaEdades / contadorIteraciones
promedioEstatura = sumaEstaturas/contadorIteraciones
cadenaReporte = f"{cadenaReporte}Promedio de edades: {promedioEdad:.2f}\n"\
f"Promedio de estaturas: {promedioEstatura:.2f}\n"
print(f"{cadenaReporte}\n")