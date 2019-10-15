"""
	append: acumulador
	autor: jecueva11
"""
# datos
datos = [1, 2, 10, 11, 12, 13]

resultado = []
# utilizacion de un condicional
for i  in datos:
	if i%2==0:
		resultado.append(i)
# imprecion del resultado
print(resultado)