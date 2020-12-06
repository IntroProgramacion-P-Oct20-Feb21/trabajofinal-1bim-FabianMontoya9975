"""
	Se pide ingresar por teclado el nombre, apellido y año de nacimiento
	del estudiante y se presentará un reporte así:

		Datos del estudiante:
		José
		Montoya
		2002
"""
nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
nacimiento = input("Ingrese el año de nacimiento del estudiante: ")
mensaje = f"Datos del estudiante:\n{nombre}\n{apellido}\n{nacimiento}\n"
print(mensaje)