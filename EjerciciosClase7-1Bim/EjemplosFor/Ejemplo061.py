"""
	Generar varias tablas de multiplicar sin utilizar cliclos
	repetitivos anidados
"""
contador = 1
cadena = ""
for contador in range(contador, 13):
	opracion = 1 * contador
	cadena = f"{cadena}1 * {contador} = {opracion}\n"
contador = 1
for contador in range(contador, 13):
	opracion = 2 * contador
	cadena = f"{cadena}2 * {contador} = {opracion}\n"
contador = 1
for contador in range(contador, 13):
	opracion = 3 * contador
	cadena = f"{cadena}3 * {contador} = {opracion}\n"
contador = 1
for contador in range(contador, 13):
	opracion = 4 * contador
	cadena = f"{cadena}4 * {contador} = {opracion}\n"
print(cadena)