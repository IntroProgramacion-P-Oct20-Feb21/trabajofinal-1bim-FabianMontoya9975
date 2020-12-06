"""
	Presentar en pantalla contador del 1 al 10 utilizando el ciclo
	repetitivo: while

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
"""
limite = 10
contador = 1
mensaje = ""
while (contador <= limite):
	mensaje = f"{mensaje}Contador {contador}\n"
	contador = contador + 1
print(mensaje)