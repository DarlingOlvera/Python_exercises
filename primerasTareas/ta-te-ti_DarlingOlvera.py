"""
    Ta Te Ti: Juego de ta te ti que muestra un tablero de 3x3 y le permite al usuario
    elegir el simbolo con el que jugará. El juego debe terminar en empate o con un ganador.

    Autor: Darling Mercedes Olvera Piña
    python version: 3.10.6
"""

#funciones

#imprimir tablero
def imprimir_tablero(matriz):
    print('|' + matriz[0][0] +'|'+'|' + matriz[0][1] +'|'+'|' + matriz[0][2] +'|')
    print('|' + matriz[1][0] +'|'+'|' + matriz[1][1] +'|'+'|' + matriz[1][2] +'|')
    print('|' + matriz[2][0] +'|'+'|' + matriz[2][1] +'|'+'|' + matriz[2][2] +'|')

#coloca la ficha en la posicion deseada
def poner_ficha(matriz,posicion,turno):
    if turno:
        ficha = 'X'
    else:
        ficha = 'O'
# para que la sentencia match funcione el programa debe correrse en python 3.10 para arriba
    match posicion:
        case 1:
            if matriz[0][0] == '1':
                matriz[0][0] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 2:
            if matriz[0][1] == '2':
                matriz[0][1] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 3:
            if matriz[0][2] == '3':
                matriz[0][2] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 4:
            if matriz[1][0] == '4':
                matriz[1][0] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 5:
            if matriz[1][1] == '5':
                matriz[1][1] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 6:
            if matriz[1][2] == '6':
                matriz[1][2] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 7:
            if matriz[2][0] == '7':
                matriz[2][0] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 8:
            if matriz[2][1] == '8':
                matriz[2][1] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case 9:
            if matriz[2][2] == '9':
                matriz[2][2] = ficha
                return 0
            else:
                return 'Posicion ocupada, intente de nuevo'
        case _:
            return 'La posicion seleccionada no existe'

#verifica si se acumple alguna de las posibles jugadas para algun jugador
def partida_ganada(matriz):
    for ficha in ['X','O']:
        f1 = matriz[0][0] == ficha and matriz[0][1] == ficha and matriz[0][2] == ficha
        f2 = matriz[1][0] == ficha and matriz[1][1] == ficha and matriz[1][2] == ficha
        f3 = matriz[2][0] == ficha and matriz[2][1] == ficha and matriz[2][2] == ficha
        c1 = matriz[0][0] == ficha and matriz[1][0] == ficha and matriz[2][0] == ficha
        c2 = matriz[0][1] == ficha and matriz[1][1] == ficha and matriz[2][1] == ficha
        c3 = matriz[0][2] == ficha and matriz[1][2] == ficha and matriz[2][2] == ficha
        d1 = matriz[0][0] == ficha and matriz[1][1] == ficha and matriz[2][2] == ficha
        d2 = matriz[2][0] == ficha and matriz[1][1] == ficha and matriz[0][2] == ficha

        if f1 or f2 or f3 or c1 or c2 or c3 or d1 or d2:
            if ficha == 'X':
                return 1
            elif ficha == 'O':
                return 2
            break

#variables
tablero = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

jugada  = 0
turno = True

#programa principal
print( '''
----------------------------------------------------------------------------------------------------------------------
Bienvenido al ta te ti en python!

    Las reglas son las siguientes:
    - Comienza el jugador_1 con la ficha X y continua el jugador_2 con la ficha O
    - Para seleccionar una posicion en el tablero simplemente ingresa el numero que se encuentra en la posicion deseada
    
Disfruta el juego
----------------------------------------------------------------------------------------------------------------------''')
imprimir_tablero(tablero)
while jugada < 9:

    if turno:
        print('Turno del jugador_1, ingresa una posicion')
    else:
        print('Turno del jugador_2, ingresa una posicion')
    
    posicion = int(input('ingrese la posicion: '))

    val = poner_ficha(tablero, posicion, turno)
    if val == 0:
        turno = not turno
        jugada += 1
        imprimir_tablero(tablero)
        if partida_ganada(tablero) == 1:
            print('Ha ganado el jugador_1')
            break
        elif partida_ganada(tablero) == 2:
            print('Ha ganado el jugador_2')
            break
    else:
        print(val)
    
    if jugada == 9:
        print('Hubo un empate...')

    

