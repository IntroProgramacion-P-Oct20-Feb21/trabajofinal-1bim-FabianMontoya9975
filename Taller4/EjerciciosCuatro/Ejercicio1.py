"""
	Generar un algoritmo que permite calcular y presentar el área de un
	triángulo. Los datos deben ser pedidos al usuario.
"""
base = float(input("Ingresar la base del triángulo: "))
altura = float(input("Ingresar la altura del triángulo: "))
producto = base * altura
cociente = producto / 2
mensaje = f"El área del triángulo es: {cociente:.3f}\n"
print(mensaje)