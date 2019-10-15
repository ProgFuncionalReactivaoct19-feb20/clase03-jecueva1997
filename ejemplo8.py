"""
	Aplicando funcion filter
	autor: jecueva11
"""
# datos
ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala", "Portoviejo", "Macas"]
# utilizacion del lambda para saber si es la longitud de los caracteres pares
resultado = filter(lambda x: len(x) % 2 ==0, ciudades)
# imprime el resultado
print(list(resultado))
