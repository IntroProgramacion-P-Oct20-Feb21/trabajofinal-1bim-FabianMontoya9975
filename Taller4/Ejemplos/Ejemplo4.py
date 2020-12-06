"""
	Se pide ingresar por teclado los siguietas datos: nombre de la asigatura 1,
	nombre de la asigatura 2, nota 1, nota 2 y nombre del estudiante. Prentar
	un reporte en pantalla como el siguiente:

	Asignatura 1:Matemáticas
	Nota 1: 8.90
	Asignatura 2:Historia
	Nota 2: 10.00
	Nombre de estudiante: José
"""
nombreAsignatura1 = input("Ingrese nombre de asignatura 1: ")
nombreAsignatura2 = input("Ingrese nombre de asignatura 2: ")
notaAsignatura1 = float(input("Ingrese nota de asignatura 1: "))
notaAsignatura2 = float(input("Ingrese nota de asignatura 2: "))
nombreEstudiante = input("Ingrese el nombre del estudiante: ")
mensaje = f"Asignatura 1: {nombreAsignatura1}\nNota 1: {notaAsignatura1:.2f}"\
f"\nAsignatura 2: {nombreAsignatura2}\nNota 2: {notaAsignatura2:.2f}\n"\
f"Nombre de estudiante: {nombreEstudiante}\n"
print(mensaje)