"""
	Generar un algoritmo que permite ingresar los gastos de tres hijos de un
	padre de familia; calcular y mostrar el total de gastos de los hijos del
	padre de familia.
"""
gasto1 = float(input("Ingresar gastos del primer hijo: $"))
gasto2 = float(input("Ingresar gastos del segundo hijo: $"))
gasto3 = float(input("Ingresar gastos del tercer hijo: $"))
suma = gasto1 + gasto2 + gasto3
mensaje = f"Es gasto total es: ${suma:.2f}\n"
print(mensaje)