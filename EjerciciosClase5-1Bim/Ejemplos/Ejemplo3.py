"""
	Realizar un programa que permita determinar si un estudiante ha pasado
	el ciclo se ingresa el promedio del estudiante
	- Si el estudiante aprueba el ciclo si tiene un promedio mayor o igual
	a 7.5
	-Si el estudiante aprueba el ciclo, presentar un mensaje como sigue.
	Estudiante aprobado con un promedio: ?
	- Si el estudiante tiene una nota mayor o igual a 5 y menor igual a 7.4
	presentar un mensaje con el siguiente texto:
	Estudiante en suspenso con un preomedio: ?
	- Si el estudiante tiene una nota menor a 5 presentar un mensaje con el
	siguiente texto: Estudiante reprobado con un promedio: ?
"""
promedio = float(input("Ingresar promedio del estudiante: "))
if promedio >= 7.5:
	mensaje = f"Estudiante aprobado con un promedio: {promedio:.2f}\n"
else:
	if ((promedio >= 5) and (promedio <= 7.4)):
		mensaje = f"Estudiante en suspenso con un promedio: {promedio:.2f}\n"
	else:
		mensaje = f"Estudiante reprobado con un promedio: {promedio:.2f}\n"
print(mensaje)