"""
	Se pide ingresar por el teclado el largo y el ancho de un terreno, el
	costo por metro cuadrado, y el nombre del comprador.
	Calcular el area del terreno y luego imprimir en pantalla un reporte como
	el siguiente:

	El costo del terreno es: $12000.00
	Nombre del comprador: José Montoya
"""
largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))
costoMetro = float(input("Ingrese el costo del m2 del terreno: $"))
nombreComprador = input("Ingresar el nombre del comprador: ")
area = largo * ancho
costoTerreno = area * costoMetro
mensaje = f"El costo del terreno es: ${costoTerreno:.2f}\n"\
f"Nombre del comprador: {nombreComprador}\n"
print(mensaje)