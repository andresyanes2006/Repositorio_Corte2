class pokemon():
    def __int__(self):
        self.nombre=None
        self.color=None
        self.categoria=None
        self.tipo=None
        self.codigo=None

    def correr(self):
        return 'estoy corriendo'
    
    def quemar(self):
        return 'estoy quemando'
    
    def volar(self):
        return 'estoy volando'

def main():
    pikachu=pokemon()
    pikachu.nombre='pikachu'
    pikachu.color='Amarillo'
    pikachu.categoria='raton'
    pikachu.tipo='Electrico'
    pikachu.codigo=25
    print(f'{pikachu.nombre}: {pikachu.correr()}\n')

    chanizar=pokemon()
    chanizar.nombre='chanizar' 
    chanizar.color='Naranja'
    chanizar.categoria='Dragon'
    chanizar.tipo='fuego'
    chanizar.codigo=6
    print(f'{chanizar.nombre}: {chanizar.quemar()}, {chanizar.volar()} \n')

    ninetales=pokemon()
    ninetales.nombre='ninetales'
    ninetales.color='Naranja'
    ninetales.categoria='Dragon'
    ninetales.tipo='fuego'
    ninetales.codigo=6
    print(f'{ninetales.nombre}: {ninetales.correr()}, {ninetales.quemar()}\n')


if __name__=='__mian__':
    main()

