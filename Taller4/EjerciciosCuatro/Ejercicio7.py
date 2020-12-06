"""
	Se debe generar un algoritmo que permite calcular y mostrar el valor total
	a pagar mensual de servicios digitales de una persona. Los servicios
	digitales son: netflix, youtube premium, dropbox, spotify. Si la persona
	es menor a 30 años se descuenta el 20% del total mensual.
"""
edad = int(input("Ingresar edad del usuario: "))
costo_netflix = float(input("Ingresar costo del servicio digital Netflix: $"))
costo_youtube = float(input("Ingresar costo del servicio digital "\
	"Youtube Premium Premium: $"))
costo_dropbox = float(input("Ingresar costo del servicio digital Dropbox: $"))
costo_spotify = float(input("Ingresar costo del servicio digital Spotify: $"))
suma = costo_netflix + costo_youtube + costo_dropbox + costo_spotify
descuento = suma * 0.2
valor_con_descuento = suma - descuento
if edad <30:
	mensaje = f"El usuario es menor a 30 años.\nEl valor total a pagar con "\
	f"el 20% de descuento es: ${valor_con_descuento:.2f}\n"
else:
	mensaje = f"El valor total a pagar es: ${suma:.2f}\n"
print(mensaje)