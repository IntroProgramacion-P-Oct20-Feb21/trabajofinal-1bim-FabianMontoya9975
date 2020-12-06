"""
	Presentar lo siguiente:
	
	*
	**
	***
	****
	*****

"""
cadena = ""
i = 1
for i in range(i, 6):
	contador = 1
	for contador in range(contador, i+1):
		cadena = f"{cadena}*"
	cadena = f"{cadena}\n"
print(cadena)