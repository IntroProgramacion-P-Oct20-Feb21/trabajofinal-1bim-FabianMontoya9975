"""
	Pedir por teclado los siguientes datos: nombre del trabajador, sueldo y
	ciudad, se va a iterar 5 veces con el ciclo repetitivo for
	Presentar el siguiente reporte:
	
	Jose (120.00) -Loja-
	Juan (213.00) -Machala-
	Mario (456.00) -Quito-
	Julio (123.00) -Loja-
	Martin (235.00) -Loja-

"""
cadena01 = ""
while (contador <= 5):
	nombre = input("Ingrese el nombre del trabajador: ")
	sueldo = float(input("Ingrese el sueldo del trabajador: "))
	ciudad = input("Ingrese la ciudad del trabajador: ")
	cadena01 = f"{cadena01}{nombre} ({sueldo:.2f}) -{ciudad}-\n"
	contador = contador + 1
print(f"{cadena01}\n")