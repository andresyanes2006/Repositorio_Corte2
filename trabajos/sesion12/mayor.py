import random as r

def M(list,index):
    if index == len(list): 
        return None
    guardado=list[index]
    maximo_siguiente = M(list, index + 1)
    if (maximo_siguiente is None) or (guardado > maximo_siguiente):       
        return guardado
    else:
        return maximo_siguiente
    
def lista():
    lista = []
    for i in range(10):
        lista.append(r.randint(0, 10))
    print(lista)
    return lista

def inicio():
    list = lista()
    mayor=M(list, 0)
    print(f'el valor mas grande es: {mayor}')

if __name__ == '__main__':
    inicio()