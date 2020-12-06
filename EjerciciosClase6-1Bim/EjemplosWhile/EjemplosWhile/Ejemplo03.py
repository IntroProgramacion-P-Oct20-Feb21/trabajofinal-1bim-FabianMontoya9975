"""
	Presentar en pantalla contador del 1 al 10 utilizando el ciclo
	repetitivo: while, y presentar al final la suna de los numeros del 1 al 10

	Contador 1
	Contador 2
	Contador 3
	Contador 4
	Contador 5
	Contador 6
	Contador 7
	Contador 8
	Contador 9
	Contador 10
	La suma final es 55

"""
limite = 10
contador = 1
suma = 0
mensaje = ""
while (contador <= limite):
	suma = suma + contador
	mensaje = f"{mensaje}Contador {contador}\n"
	contador = contador + 1
mensaje = f"{mensaje}La suma final es {suma}\n"
print(mensaje)