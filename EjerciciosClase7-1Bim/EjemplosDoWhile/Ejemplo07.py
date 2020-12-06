"""
	Presentar las tablas de multiplicar del 1 al 5

	Tabla de multiplicar del n▒mero: 1
	1 * 1 = 1
	1 * 2 = 2
	1 * 3 = 3
	1 * 4 = 4
	1 * 5 = 5
	1 * 6 = 6
	1 * 7 = 7
	1 * 8 = 8
	1 * 9 = 9
	1 * 10 = 10


	Tabla de multiplicar del n▒mero: 2
	2 * 1 = 2
	2 * 2 = 4
	2 * 3 = 6
	2 * 4 = 8
	2 * 5 = 10
	2 * 6 = 12
	2 * 7 = 14
	2 * 8 = 16
	2 * 9 = 18
	2 * 10 = 20


	Tabla de multiplicar del n▒mero: 3
	3 * 1 = 3
	3 * 2 = 6
	3 * 3 = 9
	3 * 4 = 12
	3 * 5 = 15
	3 * 6 = 18
	3 * 7 = 21
	3 * 8 = 24
	3 * 9 = 27
	3 * 10 = 30


	Tabla de multiplicar del n▒mero: 4
	4 * 1 = 4
	4 * 2 = 8
	4 * 3 = 12
	4 * 4 = 16
	4 * 5 = 20
	4 * 6 = 24
	4 * 7 = 28
	4 * 8 = 32
	4 * 9 = 36
	4 * 10 = 40


	Tabla de multiplicar del n▒mero: 5
	5 * 1 = 5
	5 * 2 = 10
	5 * 3 = 15
	5 * 4 = 20
	5 * 5 = 25
	5 * 6 = 30
	5 * 7 = 35
	5 * 8 = 40
	5 * 9 = 45
	5 * 10 = 50

"""
contador = 1
cadena = ""
while (contador <= 5):
	cadena = f"{cadena}Tabla de multiplicar del número: {contador}\n"
	i = 1
	for i in range(i, 11):
		operacion = i * contador
		cadena = f"{cadena}{contador} * {i} = {operacion}\n"
	cadena = f"{cadena}\n\n"
	contador = contador + 1
print(cadena)