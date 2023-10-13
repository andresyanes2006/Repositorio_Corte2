import random as r

def inicio():
    lista=[]
    for i in range(10):
        lista.append(r.randint(1,50))
    print(lista)
    return lista

def mayor(guardado):
    valormaximo=guardado[0]
    for i in guardado:
        if i > valormaximo:
            valormaximo=i
    print(f'El valor mas alto es: {valormaximo}')

def menor(guardado):
    valorminimo=guardado[0]
    for i in guardado:
        if i < valorminimo:
            valorminimo=i
    print(f'El valor mas bajo es: {valorminimo}')

def primos(guardado):
    pass

  
            


if __name__=='__main__':
    guardado=inicio()
    mayor(guardado)
    menor(guardado)
