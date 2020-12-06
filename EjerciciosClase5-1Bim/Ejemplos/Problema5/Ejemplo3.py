"""
	En una hosteria de la ciudad de Loja se hace un descuento del 10% 
	si el cliente se hospeda más de 5 días, del 15% si se hospeda más de 
	10 días y del 20% si se hospeda más de 15 días. 
	Elaborar un solución que pida como datos de entrada el número de días y 
	el precio diario de la habitación y luego calcule e imprima el 
	subtotal por pagar, el descuento y el total por pagar.
"""
porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20
numeroDias = int(input("Ingrese el número de días que se hospedará: "))
precioHabitacion = float(input("Ingrese el valor diario de la habitación: $"))
if ((numeroDias > 5) and (numeroDias <= 10)):
	subtotal = numeroDias * precioHabitacion
	descuento = (porcentaje1 * subtotal)/100
	valorTotal = subtotal - descuento
elif ((numeroDias > 10) and (numeroDias <= 15)):
	subtotal = numeroDias * precioHabitacion
	descuento = (porcentaje2 * subtotal)/100
	valorTotal = subtotal - descuento
elif (numeroDias > 15):
	subtotal = numeroDias * precioHabitacion
	descuento = (porcentaje3 * subtotal)/100
	valorTotal = subtotal - descuento
else:
	subtotal = numeroDias * precioHabitacion
	descuento = 0
	valorTotal = subtotal - descuento
mensaje = f"El valor subtotal es: ${subtotal:.2f}\n"\
f"El descuento es: ${descuento:.2f}\n"\
f"El valor total a pagar es: ${valorTotal:.2f}\n"
print(mensaje)