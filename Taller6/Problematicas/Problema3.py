"""
	Realizar un programa en Java que permita pedir por teclado empleados;
	se debe ingresar hasta el usuario decida ya no ingresar más empleados.
	Por cada empleado se debe solicitar el nombre, numero de días trabajados
	y costo del día trabajo. Calcular el valor a cancelar por la empresar para
	cada empleado Presentar un reporte como el siguiente:

	Nombre 1	10		$2.5	$25
	Nombre 2	11		$2		$22
	Nombre 3	9		$3		$27
	Nombre 4	5		$4		$20
	Nombre 5	12		$2		$24
"""
cadenaFinal = ""
opcion = "si"
while (opcion == "si"):
	nombre = input("Ingresar el nombre del empleado: ")
	numeroDias = int(input("Ingresar el número de días trabajados: "))
	costoDia = float(input("Ingrese el costo del Día trabajado: "))
	valorCancelar = numeroDias * costoDia
	cadenaFinal = f"{cadenaFinal}{nombre}\t{numeroDias}\t{costoDia:.2f}\t"\
	f"{valorCancelar:.2f}\n"
	opcion = input("Ingresar Si para seguir ingresando datos\n"\
		"Ingresar No para presentar el reporte final: ")
	opcion = opcion.lower()
if (opcion == "no"):
	cadenaFinal = f"{cadenaFinal}"
else:
	cadenaFinal = "Datos incorrectos\n"
print(cadenaFinal)