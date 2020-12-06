"""
	Generar un programa que permita generar la tabla de sumar o multiplicar.
	- El usuario debe ingresar si desea la tabla de sumar o restar.
	- El usuario debe ingresar el número de tabla a generar
	- El usuario debe ingresar el límite de la tabla
"""
cadenaFinal = ""
contador = 1
tipoOperacion = input("indique que tipo de tabla quiere realizar\n"\
	"suma\n"\
	"o\n"\
	"multiplicacion: ")
numeroTabla = int(input("Ingrese el número de tabla: "))
limiteTabla = int(input("Ingrese el limite de tabla: "))
if (tipoOperacion == "suma"):
	cadenaFinal = f"{cadenaFinal}Tabla de sumar\n"
	while (contador <= limiteTabla):
		operacion = numeroTabla + contador
		cadenaFinal = f"{cadenaFinal}{numeroTabla} + {contador} = "\
		f"{operacion}\n"
		contador = contador + 1
elif (tipoOperacion == "multiplicacion"):
	cadenaFinal = f"{cadenaFinal}Tabla de multiplicación\n"
	while (contador <= limiteTabla):
		operacion = numeroTabla * contador
		cadenaFinal = f"{cadenaFinal}{numeroTabla} * {contador} = "\
		f"{operacion}\n"
		contador = contador + 1
else:
	cadenaFinal = "Error en tipo de operación"
print(cadenaFinal)