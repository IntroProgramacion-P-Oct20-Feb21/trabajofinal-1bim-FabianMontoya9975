"""
	Se pide ingresar por teclado notas de los estudiantes de una materia
	Se van a seguir ingresando calificaciones hasta que el usuario decida
	ya no ingresar mas notas y para salir del ciclo se va a digitar:
	SI, Si, sI, si
	En pantalla sepresentará el promedio de todas las notas ingresadas por
	el usuario
"""
contador = 0
suma_total = 0
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
	calificacion = int(input("Ingrese calificación: "))
	suma_total = suma_total + calificacion
	contador = contador + 1
	temporal = input("Ingrese si(salir): ")
	temporal = temporal.lower()
	if (temporal == "si"):
		bandera = False
promedioFinal = suma_total / contador
mensaje = f"El promedio final es {promedioFinal:.2f}\n"
print(mensaje)