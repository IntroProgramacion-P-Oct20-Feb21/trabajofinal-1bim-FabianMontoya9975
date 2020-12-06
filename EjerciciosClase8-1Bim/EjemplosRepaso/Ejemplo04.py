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
	region = "Usted seleccionó: Región Sierra"
elif(tipoRegion == 2):
	region = "Usted seleccionó: Región Costa"
elif(tipoRegion == 3):
	region = "Usted seleccionó: Región Amazónica"
elif(tipoRegion == 4):
	region = "Usted seleccionó: Región Insular"
else:
	region = "Error, no existe región."
print(f"{region}\n")