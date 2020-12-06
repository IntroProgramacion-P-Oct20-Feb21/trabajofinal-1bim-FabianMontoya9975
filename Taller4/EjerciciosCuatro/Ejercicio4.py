"""
Generar un algoritmo que permita calcular y mostrar el costo de una
computadora de escritorio. La misma es comprada por partes; CPU, teclado,
pantalla, ratón.
"""
costo_cpu = float(input("Ingresar el costo del CPU: $"))
costo_teclado = float(input("Ingresar el costo del teclado: $"))
costo_pantalla = float(input("Ingresar el costo de la pantalla: $"))
costo_raton = float(input("Ingresar el costo del ratón: $"))
suma = costo_cpu + costo_teclado + costo_pantalla + costo_raton
mensaje = f"El costo de la computadora de escritorio es de: ${suma:.2f}\n"
print(mensaje)