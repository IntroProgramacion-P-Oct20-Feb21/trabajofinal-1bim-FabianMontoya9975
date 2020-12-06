"""
	Generar la serie: +1/1-1/3+1/5-1/7+1/9 
"""
numerador = 1
denominador = 1
contador = 1
cadena = ""
while (contador <= 5):
	if ((contador % 2) == 0):
		cadena = f"{cadena}-{numerador}/{denominador}"
	else:
		cadena = f"{cadena}+{numerador}/{denominador}"
	contador = contador + 1
	denominador = denominador + 2
cadena = f"{cadena}\n"
print(cadena)