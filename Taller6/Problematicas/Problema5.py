"""
	Realizar un programa en Java que permita ingresar 4 estudiantes; por cada
	uno de ellos ingresar el nombre del estudiante, el promedio de ciclo.
	Presentar el siguiente reporte

	Estudiante 1	10	Aprobado
	Estudiante 2	6.9	Reprobado
	Estudiante 3	7	Aprobado
	Estudiante 4	5	Reprobado

	Atención; con base al valor del promedio, usted debe asignar en cada
	registro el tipo Aprobado o Reprobado.
"""
contador = 1
cadenaFinal = ""
estadoReporte = ""
while (contador <= 4):
	nombre = input("Ingrese el nombre del estudiante: ")
	promedioCiclo = float(input("Ingrese el promedio del ciclo: "))
	if ((promedioCiclo >=0) and (promedioCiclo < 7)):
		estadoReporte = "Reprobado"
	if ((promedioCiclo >= 7) and (promedioCiclo <= 10)):
		estadoReporte = "Aprobado"
	cadenaFinal = f"{cadenaFinal}{nombre}\t{promedioCiclo:.2f}\t"\
	f"{estadoReporte}\n"
	contador = contador + 1
print(f"{cadenaFinal}\n")