"""
	Se pide ingresar por teclado notas de los estudiantes de una materia
	Se van a seguir ingresando calificaciones hasta que el usuario decida
	ya no ingresar mas notas y para salir del ciclo se va a digitar -1
	En pantalla sepresentará el promedio de todas las notas ingresadas por
	el usuario
"""
suma_total = 0
bandera = True
contador = 0
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
	calificacion = float(input("Ingrese calificación: "))
	suma_total = suma_total + calificacion
	contador = contador + 1
	temporal = int(input("Ingrese el valor de -1 para salir del ciclo: "))
	if (temporal == -1):
		bandera = False
promedioFinal = suma_total / contador
mensaje = f"El promedio final es: {promedioFinal:.2f}\n"
print(mensaje)