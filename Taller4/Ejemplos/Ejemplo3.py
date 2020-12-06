"""
	Se pide ingresar por teclado los siguietas datos: nombre de la asigatura 1,
	nombre de la asigatura 2, nota 1 y nota 2. Prentar un reporte en pantalla
	como el siguiente:

	Matemáticas
	8.90
	Historia
	10.00
"""
nombreAsignatura1 = input("Nombre Asignatura 1: ")
nombreAsignatura2 = input("Nombre Asignatura 2: ")
notaAsignatura1 = float(input("Nota Asignatura 1: "))
notaAsignatura2 = float(input("Nota Asignatura 2: "))
mensaje = f"{nombreAsignatura1}\n{notaAsignatura1:.2f}\n{nombreAsignatura2}\n"\
f"{notaAsignatura2:.2f}\n"
print(mensaje)