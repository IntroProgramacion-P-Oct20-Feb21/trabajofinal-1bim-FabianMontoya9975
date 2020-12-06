"""
	Realizar un programa que permita seleccionar el tipo de
	operación aritemética (+,-,*) a realizar para dos valores ingresados por
	teclado
	Realizar la operación y presentar el resultado en pantalla
"""
valor1 = int(input("Ingrese el primer valor la operación: "))
valor2 = int(input("Ingrese el segundo valor la operación: "))
resultado = 0
op = int(input("Selecciones la operación que desea realizar\n"\
	"Ingrese 1 para sumar\n"\
	"Ingrese 2 para restar\n"\
	"Ingrese 3 para multiplicar: "))
if (op == 1):
	resultado = valor1 + valor2
elif (op == 2):
	resultado = valor1 - valor2
elif(op == 3):
	resultado = valor1 * valor2
else:
	print("Operación incorrecta")
print(f"El resultado de la operación es : {resultado}\n")