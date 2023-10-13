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

def mn2(valor2):
    valoresfinales=[]
    for fila in valor2:
        for i in fila:
            valoresfinales.append(i)
    return valoresfinales

                                

if __name__=='__main__':
   
    mn=inicio()
    valor2=valor(mn)
    matriz1D=mn2(valor2)
    print(f'El valor maximo de la matriz es: {max(matriz1D)}, en la posicion: {matriz1D.index(max(matriz1D))}')
    print(f'El valor minimo de la matriz es: {min(matriz1D)}, en la posicion: {matriz1D.index(min(matriz1D))}')


    matrizordenada=matriz1D.sort(reverse=True)
    print('------------matriz ordenada de mayor a menor----------------')
    matriz=[]
    for i in matriz1D:
        matriz.append(i)
    print(matriz)
   