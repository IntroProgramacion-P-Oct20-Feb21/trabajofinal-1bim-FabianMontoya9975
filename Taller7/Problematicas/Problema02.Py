""""
	Generar e imprimir la siguiente serie:
	2 6 12 20 30 42 56 72 90 110
"""contador = 1
contador2 = 2
contadorElementos = 1
cadena = ""
while (contadorElementos <= 10):
	numero = contador * contador2
	cadena = f"{cadena}{numero} "
	contador = contador + 1
	contador2 = contador2 + 1
	contadorElementos = contadorElementos + 1
print(f"{cadena}\n")