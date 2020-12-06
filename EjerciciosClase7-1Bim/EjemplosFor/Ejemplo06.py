"""
	Generar la tabla de multiplicar del numero que se ingrese que va
	desde el 1 al 30
"""
tabla = int(input("Ingrese la tabla a generar: "))
contador = 5
cadena = ""
for contador in range(contador, 31):
	operacion = tabla * contador
	cadena = f"{cadena}{tabla} * {contador} = {operacion}\n"
print(cadena)