"""
	Aplicando funcion filter
	autor: jecueva11
"""
# datos
datos = [1, 2, 10, 11, 12, 13]
# utilizacion del lambda
resultado = filter(lambda x: x % 2 == 0, datos)

print(resultado)
# imprecion del resultado
print(list(resultado)) 