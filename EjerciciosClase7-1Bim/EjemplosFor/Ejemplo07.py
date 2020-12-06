"""
	Generar las tablas de multiplicar del 1 al 10, en rangos del
	1 al 12
"""
i = 1
cadena = ""
for i in range(i, 11):
	contador = 1
	cadena = f"{cadena}Tabla de multiplicar del número {i}:\n"
	for contador in range(contador, 13):
		operacion = i * contador
		cadena = f"{cadena}{i} * {contador} = {operacion}\n"
	cadena = f"{cadena}\n"
print(cadena)