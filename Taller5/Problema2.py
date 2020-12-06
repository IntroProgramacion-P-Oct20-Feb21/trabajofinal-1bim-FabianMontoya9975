"""
	Solución que imprima el costo de un pedido de un artículo del cual se
	tiene la descripción, la cantidad que se requiere y el precio unitario.
	Si la cantidad pedida excede de 50 unidades, se hace un descuento de 15%.
"""

descripcion = input("Ingresar descripción del artículo: ")
cantidad = int(input("Ingresar cantidad de unidades requeridas del "\
	"artículo: "))
precioUnitario = float(input("Ingresar el precio unitario del artículo: "))
subTotal = cantidad * precioUnitario
if (cantidad > 50):
	descuento = subTotal * 0.15  #15%
	porcentaje = "15%"
else:
	descuento = 0.00
	porcentaje = "0%"
total = subTotal - descuento
mensaje = f"Decripción: {descripcion}\n"\
f"Número de unidades requeridas: {cantidad}\n"\
f"Subtotal: ${subTotal:.2f}\nDescuento {porcentaje}: ${descuento:.2f}\n"\
f"Total a pagar: ${total:.2f}\n"
print(mensaje)