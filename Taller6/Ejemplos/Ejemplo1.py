"""
	Determine si un número es par o impar
"""
numero = 11
mensaje = ""
if ((numero % 2) == 0):
	mensaje = f"El número {numero} es par\n"
else:
	mensaje = f"El número {numero} es impar\n"
print(mensaje)