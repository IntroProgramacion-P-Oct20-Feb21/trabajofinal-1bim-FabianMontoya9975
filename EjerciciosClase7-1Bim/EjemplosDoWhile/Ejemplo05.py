"""
	Calculo de una potencia con multiplicaciones sucesivas en un ciclo
	repetitivo
"""
numero = 4
potencia = 3
resultado = 1
contador = 1
while (contador <= potencia):
	resultado = resultado * numero
	contador = contador + 1
print(f"{resultado}\n")