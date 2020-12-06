"""
	Se pide ingresar en número de tabla a generar luego presenta en pantalla
	una tabla de multiplicar como la siguiente,

	Tabla de multiplicar
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
	1 * 11 = 11
	1 * 12 = 12

"""
limite_tabla = 12
contador = 1
cadena = ""
tabla = int(input("Ingrese el número de tabla a generar: "))
cadena = f"{cadena}Tabla de multiplicar\n"
while (contador <= limite_tabla):
	operacion = tabla * contador
	cadena = f"{cadena} {tabla} * {contador} = {operacion}\n"
	contador = contador + 1
print(cadena)