"""
	Se pide ingresar por teclado notas de los estudiantes de una materia
	Se van a seguir ingresando calificaciones hasta que el usuario decida
	ya no ingresar mas notas y para salir del ciclo se va a digitar -1
	En pantalla sepresentará la suma de todas las notas ingresadas por el
	usuario
"""
suma_total = 0
bandera = True
print("Ingrese las notas de los estudiantes de su materia")
while (bandera):
	calificacion = float(input("Ingrese calificación: "))
	suma_total = suma_total + calificacion
	temporal = int(input("Ingrese el valor de -1 para salir del ciclo: "))
	if (temporal == -1):
		bandera = False
cadenaFinal = f"Suma de calificaciones es {suma_total:.2f}\n"
print(cadenaFinal)