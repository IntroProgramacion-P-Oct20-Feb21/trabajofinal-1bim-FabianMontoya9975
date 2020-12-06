"""
	Realizar un programa que permita determinar
	si un estudiante ha pasado el ciclo
	se ingresa el promedio del estudiante
	- Un estudiante pasa el ciclo si tiene un promedio
	mayor o igual a 7.5. Si el estudiante aprueba el ciclo, presentar
	un mensaje como sigue, Estudiante aprobado con un promedio: 8.1
	CASO CONTRARIO presentar un mensaje con el siguiente texto,
	Estudiante reprobado con un promedio: 7.4
"""
promedio = 7.4
if promedio >= 7.5:
    mensaje = f"Estudiante aprobado con un promedio: {promedio:.2f}\n"
    print(mensaje)
else:
    mensaje = f"Estudiante reprobado con un promedio: {promedio:.2f}\n"
    print(mensaje)