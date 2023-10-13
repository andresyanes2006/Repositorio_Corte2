def inicio():
    lista=[]
    numero=int(input('Por favor, ingrese un numeros: '))
    lista.append(numero)
    print(lista)
    return lista

def bucle(valor):
    
    opc='y'
    while opc=='y':
        opc=input('¿Desea ingresar otro valor? (y/n) ')
        if opc=='y':
            num=int(input('ingrese un numero: '))
            valor.append(num)
        elif opc=='n':
            promedio=sum(valor)/len(valor)
            print(f'el promedio es: {promedio}')
            break
        else:
            print('opcion invalida')
            opc='y'
        print(valor)


    
if __name__=='__main__':
    valor=inicio()
    bucle(valor)