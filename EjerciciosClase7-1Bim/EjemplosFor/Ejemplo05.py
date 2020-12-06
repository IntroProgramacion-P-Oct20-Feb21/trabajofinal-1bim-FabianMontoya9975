"""
	Generar un programa que permita calcular la potencia de un 
	número haciendo uso de multiplicaciones sucesivas
	Dado un número elevado a la potencia n mediante multiplicaciones 
	sucesivas es igual a
	numero elevados n = numero * numero * ... hasta n veces
	Ejemplo: 4 elevado 3
	numero = 4
	potencia = 3
	4 * 4 * 4
"""
numero = 10
potencia = 3
resultado = 1
contador = 1
for contador in range(contador, potencia + 1):
	resultado = resultado * numero
print(f"{resultado}\n")