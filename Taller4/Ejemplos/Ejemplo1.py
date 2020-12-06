"""
	Se pide ingresar por teclado datos de tipo decimas (float) y
	cadena (str)
"""
nombreAsignatura1 = input("Ingrese nombre de asignatura 1: ")
notaAsignatura1 = float(input("Ingrese nota de asignatura 1: "))
nombreAsignatura2 = input("Ingrese nombre de asignatura 2: ")
notaAsignatura2 = float(input("Ingrese nota de asignatura 2: "))
mensaje = f"Asignatura 1: {nombreAsignatura1}\nNota 1: {notaAsignatura1:.2f}"\
f"\nAsignatura 2: {nombreAsignatura2}\nNota 2: {notaAsignatura2:.2f}\n"
print(mensaje)