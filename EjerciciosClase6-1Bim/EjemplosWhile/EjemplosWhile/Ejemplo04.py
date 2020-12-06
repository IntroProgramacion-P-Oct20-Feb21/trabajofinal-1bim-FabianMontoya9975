"""
	Presentar en pantalla contador del 1 al 10 utilizando el ciclo
	repetitivo: while, y presentar al final la suna de los numeros del 1 al 10

	Contador 10
	Contador 11
	Contador 12
	Contador 13
	Contador 14
	Contador 15
	Contador 16
	Contador 17
	Contador 18
	Contador 19
	Contador 20
	La suma final es 165

"""
limite_inferior = 10
limite_superior = 20
contador = 10
suma = 0
mensaje = ""
while ((contador >= limite_inferior) and (contador <= limite_superior)):
	suma = suma + contador
	mensaje = f"{mensaje}Contador {contador}\n"
	contador = contador + 1
mensaje = f"{mensaje}La suma final es {suma}\n"
print(mensaje)