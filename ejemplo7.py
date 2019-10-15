"""
	Aplicando funcion filter
	autor: jecueva11
"""
# utilizacion de funcion
def inicial(x):
	# datos
	provincia = ["l", "p", "e", "a", "i"]
	# condicional
	if x[0] in provincia:
		return True
	else:
		return False
# datos
placas = ["lba-001", "gma-002", "azx", "ess-004", "oro-100", "mab-001", "iaj-002" ]

resultado = filter(inicial, placas)
# imprecion de resultado en una lista 
print(list(resultado))






