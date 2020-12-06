"""
	Presentar los numeros impares que existen entre el 1 y el 10
	utizando el ciclo repetitivo: while
"""
contador = 1
cadena = ""
while (contador <=10):
	cadena = f"{cadena}{contador}\n"
	contador = contador + 2
print(cadena)