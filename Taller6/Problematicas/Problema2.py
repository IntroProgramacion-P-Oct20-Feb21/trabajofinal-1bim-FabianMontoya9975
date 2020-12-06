"""
	Realizar un programa en Java que permita presentar en pantalla la siguiente
	secuencia: 1/10 2/20 3/11 4/21 5/12 6/22
"""
numerador = 1
denominador_Par = 20
denominador_Impar = 10
cadenaFinal = ""
while (numerador <= 6):
	if ((numerador %2) == 0):
		cadenaFinal = f"{cadenaFinal}{numerador} / {denominador_Par}\n"
		denominador_Par = denominador_Par + 1
	else:
		cadenaFinal = f"{cadenaFinal}{numerador} / {denominador_Impar}\n"
		denominador_Impar = denominador_Impar + 1
	numerador = numerador + 1
print(cadenaFinal)