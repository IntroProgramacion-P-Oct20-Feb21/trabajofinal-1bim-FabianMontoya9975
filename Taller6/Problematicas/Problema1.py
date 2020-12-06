"""
	(Uso de switch)
	Realizar un programa en Java que permita realizar pagos para empresas que
	ofertan streaming. El programa debe permitir pagar las mensualidades de
	las siguientes empresas: - Netflix (opción 1) - Disney Plus (opción 2)
	- Apple TV (opción 3) - Amazon Prime (opción 4) El programa es muy
	particular ya que permite pagar 2 o más mensualidades por cada transacción.
	Se debe solicitar como datos entrada: nombre del cliente, número de
	mensualidades, empresa (streaming) a la que desea cancelar.

	- El valor de la mensualidad de Netflix es $10.
	- El valor de la mensualidad de Disney Plus es $6
	- El valor de la mensualidad de Apple TV es $5
	- El valor de la mensualidad de Amazon Prime es $4.50

	Se debe considerar que para obtener el valor de la mensualidad a cancelar
	se debe agregar un impuesto de acuerdo a las siguientes consideraciones:
	- Netflix es 10 % de iva. - Disney Plus es 12 % de iva.
	- Apple TV es 14 % de iva. - Amazon Prime es 16 % de iva.
	Un reporte ejemplo sería el siguiente:

	Usuario: Jośe Valencia
	Empresa: Netflix
	Precio Base: $10
	Impuesto: $1
	Total a cancelar: $11

"""
base_Netflix = 10
base_Disney = 6
base_Apple = 5
base_Amazon = 4.50
cadenaFinal = ""
nombre = input("Ingresar el nombre del cliente: ")
numero_Mensualidades = int(input("Ingresar el número de mensualidades a "\
	"pagar (minimo 2): "))
if (numero_Mensualidades >= 2):
	opcion = int(input("Ingresar la opción segun la empresa de "\
		"Streaming que desea cancelar el servicio.\n"\
		"Ingresar 1 para escoger Netflix\n"\
		"Ingresar 2 para escoger Disney Plus\n"\
		"Ingresar 3 para escoger Apple TV\n"\
		"Ingresar 4 para escoger Amazon Prime: "))
	total_mes_Netflix = numero_Mensualidades * base_Netflix
	total_mes_Disney = numero_Mensualidades * base_Disney
	total_mes_Apple = numero_Mensualidades * base_Apple
	total_mes_Amazon = numero_Mensualidades * base_Amazon
	iva_Netflix = total_mes_Netflix * 0.1; #10%
	iva_Disney = total_mes_Disney * 0.12;  #12%
	iva_Apple = total_mes_Apple * 0.14;  #14%
	iva_Amazon = total_mes_Amazon * 0.16;  #16%
	total_Netflix = total_mes_Netflix + iva_Netflix
	total_Disney = total_mes_Disney + iva_Disney
	total_Apple = total_mes_Apple + iva_Apple
	total_Amazon = total_mes_Amazon + iva_Amazon
	if (opcion == 1):
		cadenaFinal = f"{cadenaFinal}Usuario: {nombre}\n"\
		f"Empresa: Netflix\n"\
		f"Número de mensualidades a pagar: {numero_Mensualidades}\n"\
		f"Precio Base (mensual): ${base_Netflix:.2f}\n"\
		f"Total de {numero_Mensualidades} mensualidad/es: "\
		f"${total_mes_Netflix:.2f}\nImpuesto: ${iva_Netflix:.2f}\n"\
		f"Total a cancelar: ${total_Netflix:.2f}\n"
	elif (opcion == 2):
		cadenaFinal = f"{cadenaFinal}Usuario: {nombre}\n"\
		f"Empresa: Disney Plus\n"\
		f"Número de mensualidades a pagar: {numero_Mensualidades}\n"\
		f"Precio Base (mensual): ${base_Disney:.2f}\n"\
		f"Total de {numero_Mensualidades} mensualidad/es: "\
		f"${total_mes_Disney:.2f}\nImpuesto: ${iva_Disney:.2f}\n"\
		f"Total a cancelar: ${total_Disney:.2f}\n"
	elif (opcion == 3):
		cadenaFinal = f"{cadenaFinal}Usuario: {nombre}\n"\
		f"Empresa: Apple TV\n"\
		f"Número de mensualidades a pagar: {numero_Mensualidades}\n"\
		f"Precio Base (mensual): ${base_Apple:.2f}\n"\
		f"Total de {numero_Mensualidades} mensualidad/es: "\
		f"${total_mes_Apple:.2f}\nImpuesto: ${iva_Apple:.2f}\n"\
		f"Total a cancelar: ${total_Apple:.2f}\n"
	elif (opcion == 4):
		cadenaFinal = f"{cadenaFinal}Usuario: {nombre}\n"\
		f"Empresa: Amazon Prime\n"\
		f"Número de mensualidades a pagar: {numero_Mensualidades}\n"\
		f"Precio Base (mensual): ${base_Amazon:.2f}\n"\
		f"Total de {numero_Mensualidades} mensualidad/es: "\
		f"${total_mes_Amazon:.2f}\nImpuesto: ${iva_Amazon:.2f}\n"\
		f"Total a cancelar: ${total_Amazon:.2f}\n"
	else:
		cadenaFinal = f"{cadenaFinal}Datos erroneos\n"
else:
	cadenaFinal = f"{cadenaFinal}Datos erroneos\n"
print(cadenaFinal)