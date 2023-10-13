import random as r

def inicio():
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(10):
            matriz[i].append(r.randint(0,50))
        print(matriz[i])
    return matriz

def valor(mn):
    matriz2=[]
    for i in range(len(mn)):
        matriz2.append([])
        for j in range(len(mn[i])):
            matriz2[i].append(mn[i][j])
    return matriz2
                                

if __name__=='__main__':
   
    mn=inicio()
    valor2=valor(mn)
    
    valoresfinales=[ i for  fila in valor2 for i in fila]
    print(f'el mayor valor es: {max(valoresfinales)}, posicion es: {valoresfinales.index(max(valoresfinales))}')
    print(f'el menor valor es: {min(valoresfinales)}, posicion es: {valoresfinales.index(min(valoresfinales))}')

    variable=valoresfinales.sort()
    print('--------matriz organizada en forma ascendente----------')
    matriz=[]
    for i in valoresfinales:
        matriz.append(i)
    print(matriz)

    