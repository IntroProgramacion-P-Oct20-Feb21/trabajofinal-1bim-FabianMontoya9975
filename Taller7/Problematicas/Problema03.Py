"""
	Generar e imprimir la siguiente serie:
	2 5 10 17 26 37
"""
contador = 3
contadorElementos = 1
numero = 2
cadena = ""
cadena = f"{cadena}{numero} "
while (contadorElementos <= 5):
	numero = numero + contador
	cadena = f"{cadena}{numero} "
	contador = contador + 2
	contadorElementos = contadorElementos + 1
print(f"{cadena}\n")