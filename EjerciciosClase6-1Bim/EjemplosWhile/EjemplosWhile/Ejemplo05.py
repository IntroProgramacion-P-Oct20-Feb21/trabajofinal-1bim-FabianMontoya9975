"""
	Utilizando el ciclo repetitivo while se pide ingresar por teclado 3 notas
	y se debe presentar en pantalla el promedio de las 3 notas ingresadas.
"""
limite = 3
contador = 1
suma_total = 0
mensaje = ""
print("Ingrese las notas de los estudiantes de su materia")
while (contador <= limite):
	calificacion = int(input(f"Ingrese calificación número {contador}: "))
	suma_total = suma_total + calificacion
	contador = contador + 1
promediofinal = suma_total / limite
mensaje = f"{mensaje}El promedio final es {promediofinal:.2f}\n"
print(mensaje)