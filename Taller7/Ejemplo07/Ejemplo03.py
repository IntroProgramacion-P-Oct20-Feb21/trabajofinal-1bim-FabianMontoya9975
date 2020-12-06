"""
	El ciclo se va a répetir hasta el usuario decida salir del ciclo
	digitando: SI, Si, sI, si
"""
bandera = True
while (bandera):
	salir = input("Desea salir del ciclo; digite: si: ")
	salir = salir.lower()
	if (salir == "si"):
		bandera = False