"""
	Generar un solución que permita calcular y mostrar el pago mensual de un
	préstamo de 1 año de plazo. Se debe ingresar el monto del préstamo y el
	interés mensual a cobrar.
"""
monto_prestamo = float(input("Ingresar el monto del préstamo: $"))
interes_mensual = float(input("Ingresar el interés mensual a cobrar: $"))
cociente = monto_prestamo / 12
suma = cociente + interes_mensual
mensaje = f"El pago mensual a pagar es: ${suma:.2f}\n"
print(mensaje)