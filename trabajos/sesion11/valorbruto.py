def VBF(list):
    
    while 1:
        opc=input('quiere saber el percio bruto del alimento(y/n): ')
        if opc=='y':
            eleccion=input('ingrese el codigo del alimento: ')
            for fila in list:
                verificar1=eleccion in fila
                verificar2= '0' in fila 
                verificar3='0.05' in fila
                verificar4='0.19' in fila 
                if verificar1 and verificar2:
                    valor=int(input('ingrese el valor del producto: '))
                    print(f'el valor bruto del producto es: {valor} \n')
                elif verificar1 and verificar3:
                    valor=int(input('ingrese el valor del producto: '))
                    iva= valor/1.05
                    print(f'el valor bruto del producto es: {iva} \n')
                elif verificar1 and verificar4:
                    valor=int(input('ingrese el valor del producto: '))
                    iva= valor/1.19
                    print(f'el valor bruto del producto es: {iva} \n')
        elif opc=='n':
            break
        else:
            print('opcion invalida')

def lista1():
    menu = open('Alimentos.txt', 'rt')
    documento = menu.readlines()
    lista = []
    for valor in documento:
        sublist = valor.strip('\n').split(',')
        lista.append(sublist)

    return lista

if __name__ == '__main__':
    list = lista1()
    for sublist in list:
        print(sublist)
    VBF(list)