"""
	El siguiente programa muestra de forma infinita la frase:
    Usted está en el ciclo
    El usuario decide si quiere seguir en el ciclo
    El usuario podrá salir con las siguiente opciones:
    SI
    Si
    SI
    si
    sI
    S
    s
"""
bandera = True
while (bandera):
	salir = input("Usted está en el ciclo\n"\
		"Si desea salir del ciclo, digite Si ó S: ")
	salir = salir.lower()
	if ((salir == "si") or (salir == "s")):
		bandera = False