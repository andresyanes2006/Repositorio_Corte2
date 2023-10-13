def posiciones(a, b, inicio=0, posicion=None):
    if posicion is None:
        posicion = []

    indice = a.find(b, inicio)

    if indice != -1:
        posicion.append(indice)
        inicio = indice + 1
        posiciones(a, b, inicio, posicion)

    return posicion

# Ejemplo de uso:
a=input('por favor ingrese una palabra: ')
b =input('por favor ingrese la palabra o letra que desea encontrar las posiciones: ')
result = posiciones(a, b)
print(result)  # Debería imprimir [0, 3, 5, 7, 10]
