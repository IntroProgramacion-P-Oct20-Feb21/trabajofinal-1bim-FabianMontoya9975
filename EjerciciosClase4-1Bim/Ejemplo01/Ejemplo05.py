"""
	Se utiliza el salto de linea y el tabulador parta dar espacio entre
	variables para presentar enm pantalla
"""
nombreEstudiante = "José Fabián"
apellidoEstudiante = "Montoya Montoya"
nacimiento = 2002
cadena1 = f"{nombreEstudiante}\n\n{apellidoEstudiante}\n\n{nacimiento}"
cadena2 = f"{nombreEstudiante}\t\t{apellidoEstudiante}"
print(f"{cadena1}\n{cadena2}")