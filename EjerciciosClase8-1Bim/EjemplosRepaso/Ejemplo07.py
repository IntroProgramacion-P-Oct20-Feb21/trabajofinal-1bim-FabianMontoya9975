"""
	El siguiente programa muestra la siguiente salida:
    10 + 1 = 11
    10 * 1 = 10
    10 + 2 = 12
    10 * 2 = 20
    10 + 3 = 13
    10 * 3 = 30
    10 + 4 = 14
    10 * 4 = 40
    10 + 5 = 15
    10 * 5 = 50
    
    Modificar el código para obtener la siguiente salida:
    10 + 1 = 11
    10 + 2 = 12
    10 + 3 = 13
    10 + 4 = 14
    10 + 5 = 15

    10 * 1 = 10
    10 * 2 = 20
    10 * 3 = 30
    10 * 4 = 40
    10 * 5 = 50
"""
tabla = 10
cadena01 = ""
cadena02 = ""
for i in range(1,5+1):
	operacion01 = tabla + i
	operacion02 = tabla * i
	cadena01 = f"{cadena01}{tabla} + {i} = {operacion01}\n"
	cadena02 = f"{cadena02}{tabla} * {i} = {operacion02}\n"
cademaFinal = f"{cadena01}\n{cadena02}"
print(cademaFinal)