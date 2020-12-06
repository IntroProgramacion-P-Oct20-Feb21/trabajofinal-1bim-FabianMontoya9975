"""
	Genere y presente el resultado en pantalla de la siguiente expresión:
		____
	   V 81  + 9						   100      _____
	(------------- == 9) or (10 > 1) and (------ + V 100  )
	      3									25
"""
resultado = (((81**(1.0/2)+9)/3)==9) or (10>1) and (100/25+100**(1.0/2)>=14)
print(resultado)