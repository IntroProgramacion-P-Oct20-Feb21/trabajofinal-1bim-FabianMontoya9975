"""
	Generar un programa que permita ingresar el número de día de la semana;
	(1 - 7)
	Si el usuario ingresa el 1, debe presentar el mensaje: Día 1  es Lunes
	Si el usuario ingresa el 2, debe presentar el mensaje: Día 2  es Martes
	Si el usuario ingresa el 3, debe presentar el mensaje: Día 3  es Miércoles
	Si el usuario ingresa el 4, debe presentar el mensaje: Día 4  es Jueves
	Si el usuario ingresa el 5, debe presentar el mensaje: Día 5  es Viernes
	Si el usuario ingresa el 6, debe presentar el mensaje: Día 6  es Sábado
	Si el usuario ingresa el 7, debe presentar el mensaje: Día 7  es Domingo
	Si el usuario ingresa un número diferente de 1,2,3,4,5,6,7; debe presentar
	un mensaje: Opción incorrecta
"""
numeroDia = int(input("Ingrese el número de día de la semana: "))
if (numeroDia == 1):
	cadena = f"Día {numeroDia} es Lunes\n"
elif (numeroDia == 2):
	cadena = f"Día {numeroDia} es Martes\n"
elif (numeroDia == 3):
	cadena = f"Día {numeroDia} es Miércoles\n"
elif (numeroDia == 4):
	cadena = f"Día {numeroDia} es Jueves\n"
elif (numeroDia == 5):
	cadena = f"Día {numeroDia} es Viernes\n"
elif (numeroDia == 6):
	cadena = f"Día {numeroDia} es Sábado\n"
elif (numeroDia == 7):
	cadena = f"Día {numeroDia} es Domingo\n"
else:
	cadena = "Opción incorrecta"
print(cadena)