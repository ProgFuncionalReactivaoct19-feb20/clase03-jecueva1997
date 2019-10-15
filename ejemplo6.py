"""
	Aplicando funcion filter
	autor: jecueva11
"""
# datos
palabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]
# utilizacion del lambda 
palindromas = filter(lambda x: x == "".join(reversed (x)), palabras)
# imprecion de resultados
print(list(palindromas))