"""
	Realizar un programa que permita determinar
	si un estudiante ha pasado el ciclo
	Se ingresa el promedio del estudiante
	- Un estudiante pasa el ciclo si tiene un promedio
	mayoy o igual a 7.5. Si el estudiante aprueba el ciclo, presentar
	un mensaje como sigue:

	Estudiante aprobado con un promedio: 8.1
"""
promedio = 8.1
if (promedio >= 7.5):
	mensaje = f"Estudiante aprobado con un promedio: {promedio:.2f}\n"
	print(mensaje)