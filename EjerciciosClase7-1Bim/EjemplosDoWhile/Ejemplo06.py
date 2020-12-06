"""
	Genere la tabla de multiplicar de un número
	que empiece desde 1 hasta 10.
	
	2 x 1 = 2
	2 x 2 = 4
	2 x 3 = 6
	2 x 4 = 8
	2 x 5 = 10
	2 x 6 = 12
	2 x 7 = 14
	2 x 8 = 16
	2 x 9 = 18
	2 x 10 = 20
"""
contador = 1
cadenaFinal = ""
tabla = int(input("Ingrese la tabla a generar: "))
while (contador <= 10):
	operacion = tabla * contador
	cadenaFinal = f"{cadenaFinal}{tabla} * {contador} = {operacion}\n"
	contador = contador + 1
print(cadenaFinal)