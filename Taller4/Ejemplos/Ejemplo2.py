"""
	Se pide ingresar por teclado los siguietas datos: nombre de la asigatura 1,
	nota 1, nombre de la asigatura 2 y nota 2. Finalmente prentar un reporte
	como el siguiente:

	Asignatura 1: Matemáticas
	Nota 2: 8.90
	Asignatura 2: Historia
	Nota 2: 10.00
"""
nombreAsignatura1 = input("Ingrese nombre de asignatura 1: ")
notaAsignatura1 = float(input("Ingrese nota de asignatura 1: "))
nombreAsignatura2 = input("Ingrese nombre de asignatura 2: ")
notaAsignatura2 = float(input("Ingrese nota de asignatura 2: "))
mensaje = f"Asignatura 1: {nombreAsignatura1}\nNota 1: {notaAsignatura1:.2f}\n"\
f"Asignatura 2: {nombreAsignatura2}\nNota 2: {notaAsignatura2:.2f}\n"
print(mensaje)