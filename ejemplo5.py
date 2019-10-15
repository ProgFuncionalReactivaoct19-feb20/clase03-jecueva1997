"""
	Aplicando funcion filter
	autor: jecueva11
"""
# utilizacion de una funcion 
def es_vocal(x):
	# datos
	vocales = [ "a", "e", "i", "o", "u"]
	# condicional
	if x in vocales:
		return True
	else:
		return False
# datos
datos = ["e", "c", "u", "a", "d", "o", "r"]

resultado = filter(es_vocal, datos)
# imprecion del resultado
print(list(resultado))