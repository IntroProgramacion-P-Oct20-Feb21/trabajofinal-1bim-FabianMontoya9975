"""
	El ciclo se va a répetir hasta el usuario decida salir del ciclo
	digitando algo diferente a: SI, Si, sI, si
"""
bandera = True
while (bandera):
	salir = input("Desea seguir en el ciclo; digite: si: ")
	salir = salir.lower()
	if (salir != "si"):
		bandera = False