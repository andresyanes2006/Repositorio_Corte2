import random as r


def inicio(lista,columnas):
    matriz=[]
    for i in range(lista):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r.randint(1,10)) 
        print(matriz[i])
    return matriz

def escalar(matriz):
    solicitud=int(input('ingrese escalar: '))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]*=solicitud
        print(matriz[i])

    

if __name__=='__main__':
   filas=int(input('Ingrese el numero de filas: '))
   columnas=int(input('Ingrese el numero de columnas: '))
   print('----------original----------')
   matriz=inicio(filas,columnas)
   print('-----------con escalar--------- ')
   escalar(matriz)
