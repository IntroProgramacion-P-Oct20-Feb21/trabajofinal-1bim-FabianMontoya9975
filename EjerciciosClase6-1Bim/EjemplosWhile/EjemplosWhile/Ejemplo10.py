"""
	Se pide ingresar en número de tabla a generar luego presenta en pantalla
	una tabla de multiplicar como la siguiente,

	Tabla de multiplicar:
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
	2 * 11 = 22
	2 * 12 = 24


"""
limite_tabla = 12
contador = 1
cadena = ""
tabla = int(input("Ingrese el número de tabla a generar: "))
cadena = f"{cadena}Tabla de multiplicar:\n"
while (contador <= limite_tabla):
	operacion = tabla * contador
	cadena = f"{cadena} {tabla} * {contador} = {operacion}\n"
	contador = contador + 1
print(cadena)