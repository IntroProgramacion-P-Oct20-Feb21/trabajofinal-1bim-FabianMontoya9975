"""
	Las entradas son: ciudad Loja, pais Ecuador
	La salida del programa debe ser así:
	   
	Loja, situada en el sur del país:
	    
		ECUADOR.
"""
ciudad = input("Ingresar la ciudad: ")
pais = input("Ingresar el país: ")
pais = pais.upper()
print(f"{ciudad}, situada en el sur del país:\n\n\t{pais}.\n")