"""
	Ingrese una cadena de texto y verifique que pertenece a un  de un día de
	la semana.
"""
cadena = input("Ingrese el nombre del día de la semana: ")
if ((cadena == "Lunes") or (cadena == "lunes")):
	mensaje = f"{cadena}\n"
elif ((cadena == "Martes") or (cadena == "martes")):
	mensaje = f"{cadena}\n"
elif ((cadena =="Jueves") or (cadena == "jueves")):
	mensaje = f"{cadena}\n"
else:
	mensaje = "Ninguna de las anteriores"
print(mensaje)