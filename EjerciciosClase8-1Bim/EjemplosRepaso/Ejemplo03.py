"""
	Cuando el usuario ingrese un valor diferente de 1,2,3,4 debe salir un
    mensaje que diga: 
    Error, no existe región.
"""
tipoRegion = int(input("Ingrese el tipo los siguientes datos para imprimir "\
	"la región del Ecuador.\n"\
	"1 para Región Sierra\n"\
	"2 para Región Costa\n"\
	"3 para Región Amazónica\n"\
	"4 para Región Insular: "))
if (tipoRegion == 1):
	region = "Región Sierra"
elif(tipoRegion == 2):
	region = "Región Costa"
elif(tipoRegion == 3):
	region = "Región Amazónica"
elif(tipoRegion == 4):
	region = "Región Insular"
else:
	region = "Error, no existe región."
if ((tipoRegion >=0) and (tipoRegion <= 4)):
	cadena = f"Usted seleccionó: {region}\n"
else:
	cadena = region
print(f"{cadena}\n")