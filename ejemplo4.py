"""
	Aplicando funcion filter
	autor: jecueva11
"""
# datos
datos = [18, 19, 20, 10, 11, 12]
# utilizacion de lambda para el proceso
resultado = filter(lambda x: x >= 18 or x <= 10, datos)
print(resultado)
# imprecion del resultado
print(list(resultado))