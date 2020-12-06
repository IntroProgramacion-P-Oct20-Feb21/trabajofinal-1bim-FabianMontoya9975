"""
	Generar, imprimira y obtenga el resultado de la serie:
	1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15
"""
numerador = 1
contadorDenominador = 3
cadena = ""
operacion = 0
cadena = f"{cadena}{numerador}"
operacion = operacion + numerador
i = 1
for i in range(i, 8):
	if ((i % 2) == 0):
		cadena = f"{cadena} + {numerador}/{contadorDenominador}"
		operacion = operacion + numerador / contadorDenominador
	else:
		cadena = f"{cadena} - {numerador}/{contadorDenominador}"
		operacion = operacion - numerador / contadorDenominador
	contadorDenominador = contadorDenominador + 2
cadena = f"{cadena} = {operacion:.3f}"
print(f"{cadena}\n")