"""
Presentar la siguiente secuencia:

*****
****
***
**
*

"""
cadena = ""
i = 5
for i in range(i, 0, -1):
	contador = 1
	for contador in range(contador, i+1):
		cadena = f"{cadena}*"
	cadena = f"{cadena}\n"
print(cadena)