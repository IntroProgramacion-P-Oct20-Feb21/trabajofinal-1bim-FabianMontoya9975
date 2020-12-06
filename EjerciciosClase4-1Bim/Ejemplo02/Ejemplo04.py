"""
	Se pide ingresar por teclado los siguientes datos: Nombres y Apellidos
	completos, ciudad de nacimiento, país de nacimiento y año de nacimiento y
	presentar un informe como el siguiente:

	Sus datos personales:
	José Fabián Montoya Montoya
	Loja-Ecuador
	2002

"""
nombres = input("Por favor, ingrese sus nombres completos: ")
apellidos = input("Por favor, ingrese sus apellidos completos: ")
ciudadnacimiento = input("Por favor, ingrese su ciudad de nacimiento: ")
paisnacimiento = input("Por favor, ingrese su país de nacimiento: ")
añonacimiento = input("Por favor, ingrese su año de nacimiento: ")
mensaje = f"Sus datos personales:\n{nombres} {apellidos}\n{ciudadnacimiento}"\
f"-{paisnacimiento}\n{añonacimiento}\n"
print(mensaje)