"""
	Determine si un número es par o impar; de un rango de números del 1 al 10
"""
contador = 1
mensaje = ""
while (contador <= 10):
	if ((contador % 2) == 0):
		mensaje = f"{mensaje}El número {contador} es par\n"
	else:
		mensaje = f"{mensaje}El número {contador} es impar\n"
	contador = contador + 1
print(mensaje)