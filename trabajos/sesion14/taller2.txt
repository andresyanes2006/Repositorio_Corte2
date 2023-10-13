def archivo():
    f = open('wcm.csv', 'r', encoding='utf8')
    documento = f.readlines()
    f.close()
    lista = []
    for valor in documento:
        dato = valor.strip('\n').split(',')
        lista.append(dato)
    return lista

def contar_enfrentamientos(x, equipo1, equipo2):
    contador = 0
    for valor in x:
        if ((equipo1 in (valor[0], valor[1])) and (equipo2 in (valor[0], valor[1]))):
            contador += 1
            print(f'-({valor[15]}-{valor[16]})-')
            print(f'{valor[0]}  |{valor[2]}vs{valor[4]}|  {valor[1]} - randa: {valor[12]}')
    print('-------------------------PARTIDOS----------------------------------')
    print(f'Cantidad de partidos: {contador} veces en los mundiales.')

def promedio_goles(x, consulta):
    total_goles_a_favor = 0
    total_partidos = 0

    for valor in x:
        equipo_local = valor[0]
        equipo_visitante = valor[1]
        goles_local = int(valor[2])
        goles_visitante = int(valor[4])

        if equipo_local == consulta:
            total_goles_a_favor += goles_local
            total_partidos += 1

        if equipo_visitante == consulta:
            total_goles_a_favor += goles_visitante
            total_partidos += 1

    if total_partidos > 0:
        promedio = total_goles_a_favor / total_partidos
        return promedio
    else:
        return 0

def inicio():
    lista_0 = archivo()
    while True:
        print('Menu:')
        print('1. Contar enfrentamientos entre equipos')
        print('2. Calcular el promedio de goles a favor de un equipo')
        print('3. Salir')
        opcion = input('Elija una opción: ')

        if opcion == '1':
            equipo1 = input('Digite el primer equipo: ')
            equipo2 = input('Digite el segundo equipo: ')
            contar_enfrentamientos(lista_0, equipo1, equipo2)
        elif opcion == '2':
            consulta = input('Ingrese el nombre del país para calcular el promedio de goles a favor: ')
            promedio_goles_a_favor = promedio_goles(lista_0, consulta)
            if promedio_goles_a_favor > 0:
                print(f'El promedio de goles a favor de {consulta} en todos los mundiales es de {promedio_goles_a_favor:.2f} goles por partido.')
            else:
                print(f'{consulta} no ha participado en ningún mundial o no ha anotado goles.')
        elif opcion == '3':
            break
        else:
            print('Opción no válida. Por favor, elija una opción válida.')

if __name__ == '__main__':
    inicio()
