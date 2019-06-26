from os import system
import random
def tablero():
    print ('  ', end = '')
    for a in range (longitud):
        print (chr(65+a), end = ' ')
    print ()
    for a in range (longitud):
        print (chr(65+a), end = '  ')
        for c in range (longitud):
            print (mat[a][c], end = ' ')
        print ()
    print ()
def turnos_jugador(cuerpo, cabeza):
    global a, b
    dir = str(input('Ingrese una dirección(arriba(w), abajo(s), izquierda(a), derecha(d): '))
    while True:
        while dir != 'arriba' and dir != 'abajo' and dir != 'izquierda' and dir != 'derecha' and dir != 'w' and dir != 's' and dir != 'a' and dir != 'd':
            dir = str(input('Error, ingrese una dirección válida: '))
        if (a == (longitud - 1) and (dir == 'abajo' or dir == 's')) or (a == 0 and (dir == 'arriba' or dir == 'w')) or (b == (longitud - 1) and (dir == 'derecha' or dir == 'd')) or (b == 0 and (dir == 'izquierda' or dir == 'a')):
            e = -(longitud - 1)
        else:
            e = 1
        mat[a][b] = cuerpo
        if ((dir == 'arriba' or dir == 'w') and (mat[a-e][b] != '_')) or ((dir == 'abajo' or dir == 's') and (mat[a+e][b] != '_' )) or ((dir == 'izquierda' or dir == 'a') and (mat[a][b-e] != '_')) or ((dir == 'derecha' or dir == 'd') and (mat[a][b+e] != '_')):
            dir = ''
            continue
        if dir == 'arriba' or dir == 'w':
            a -= e
        elif dir == 'abajo' or dir == 's':
            a += e
        elif dir == 'izquierda' or dir == 'a':
            b -= e
        else:
            b += e
        mat[a][b] = cabeza
        break
def turnos_jugador2(cuerpo, cabeza):
    global c, d
    dir = ' '
    while True:
        if jugadores == 'no':
            dir = random.choice('wasd')
        elif jugadores == 'si' and dir != '':
            dir = str(input('Ingrese una dirección(arriba(w), abajo(s), izquierda(a), derecha(d): '))
        while dir != 'arriba' and dir != 'abajo' and dir != 'izquierda' and dir != 'derecha' and dir != 'w' and dir != 's' and dir != 'a' and dir != 'd':
            dir = str(input('Error, ingrese una dirección válida: '))
        if (c == (longitud - 1) and (dir == 's')) or (c == 0 and (dir == 'w')) or (d == (longitud - 1) and (dir == 'd')) or (d == 0 and (dir == 'a')):
            e = -(longitud - 1)
        else:
            e = 1
        mat[c][d] = cuerpo
        if ((dir == 'arriba' or dir == 'w') and (mat[c-e][d] != '_')) or ((dir == 'abajo' or dir == 's') and (mat[c+e][d] != '_' )) or ((dir == 'izquierda' or dir == 'a') and (mat[c][d-e] != '_')) or ((dir == 'derecha' or dir == 'd') and (mat[c][d+e] != '_')):
            if jugadores == 'si':
                dir = ''
            continue
        if dir == 'w':
            c -= e
        elif dir == 's':
            c += e
        elif dir == 'a':
            d -= e
        else:
            d += e
        mat[c][d] = cabeza
        break
def validar_jugador(jugador):
    global jugadores, empate, repetir
    if (((a == 0) and (mat[longitud - 1][b] != '_' and mat[a + 1][b] != '_')) or ((a == (longitud - 1)) and (mat[0][b] != '_' and mat[a - 1][b] != '_')) or ((a != (longitud - 1) and a != 0) and (mat[a + 1][b]) != '_' and (mat[a - 1][b]) != '_')) and (((b == 0) and (mat[a][longitud - 1] != '_' and mat[a][b + 1] != '_')) or ((b == (longitud - 1)) and (mat[a][0] != '_' and mat[a][b - 1] != '_')) or ((b != (longitud - 1) and b != 0) and (mat[a][b + 1] != '_' and mat[a][b - 1] != '_'))) and (((c == 0) and (mat[longitud - 1][d] != '_' and mat[c + 1][d] != '_')) or ((c == (longitud - 1)) and (mat[0][d] != '_' and mat[c - 1][d] != '_')) or ((c != (longitud - 1) and c != 0) and ((mat[c + 1][d]) != '_' and (mat[c - 1][d]) != '_'))) and (((d == 0) and (mat[c][longitud - 1] != '_' and mat[c][d + 1] != '_')) or ((d == (longitud - 1)) and (mat[c][0] != '_' and mat[c][d - 1] != '_')) or ((d != (longitud - 1) and d != 0) and (mat[c][d + 1] != '_' and mat[c][d - 1] != '_'))):
        jugadores = ''
        empate = 'si'
        system('cls')
        print ('Es un empate')
        repetir = str(input('¿Desea jugar otra vez?: '))
        while repetir != 'si' and repetir != 'no':
            repetir = str(input('Error, ingrese si o no: '))
    elif (((a == 0) and (mat[longitud - 1][b] != '_' and mat[a + 1][b] != '_')) or ((a == (longitud - 1)) and (mat[0][b] != '_' and mat[a - 1][b] != '_')) or ((a != (longitud - 1) and a != 0) and (mat[a + 1][b]) != '_' and (mat[a - 1][b]) != '_')) and (((b == 0) and (mat[a][longitud - 1] != '_' and mat[a][b + 1] != '_')) or ((b == (longitud - 1)) and (mat[a][0] != '_' and mat[a][b - 1] != '_')) or ((b != (longitud - 1) and b != 0) and (mat[a][b + 1] != '_' and mat[a][b - 1] != '_'))):
        jugadores = ''
        system('cls')
        tablero()
        print('El ganador es', jugador,'\n')
        repetir = str(input('¿Desea jugar otra vez?: '))
        while repetir != 'si' and repetir != 'no':
            repetir = str(input('Error, ingrese si o no: '))
def validar_jugador2(jugador):
    global jugadores, empate, repetir
    if (((a == 0) and (mat[longitud - 1][b] != '_' and mat[a + 1][b] != '_')) or ((a == (longitud - 1)) and (mat[0][b] != '_' and mat[a - 1][b] != '_')) or ((a != (longitud - 1) and a != 0) and (mat[a + 1][b]) != '_' and (mat[a - 1][b]) != '_')) and (((b == 0) and (mat[a][longitud - 1] != '_' and mat[a][b + 1] != '_')) or ((b == (longitud - 1)) and (mat[a][0] != '_' and mat[a][b - 1] != '_')) or ((b != (longitud - 1) and b != 0) and (mat[a][b + 1] != '_' and mat[a][b - 1] != '_'))) and (((c == 0) and (mat[longitud - 1][d] != '_' and mat[c + 1][d] != '_')) or ((c == (longitud - 1)) and (mat[0][d] != '_' and mat[c - 1][d] != '_')) or ((c != (longitud - 1) and c != 0) and ((mat[c + 1][d]) != '_' and (mat[c - 1][d]) != '_'))) and (((d == 0) and (mat[c][longitud - 1] != '_' and mat[c][d + 1] != '_')) or ((d == (longitud - 1)) and (mat[c][0] != '_' and mat[c][d - 1] != '_')) or ((d != (longitud - 1) and d != 0) and (mat[c][d + 1] != '_' and mat[c][d - 1] != '_'))):
        jugadores = ''
        empate = 'si'
        system('cls')
        print ('Es un empate')
        repetir = str(input('¿Desea jugar otra vez?: '))
        while repetir != 'si' and repetir != 'no':
            repetir = str(input('Error, ingrese si o no: '))
    elif (((c == 0) and (mat[longitud - 1][d] != '_' and mat[c + 1][d] != '_')) or ((c == (longitud - 1)) and (mat[0][d] != '_' and mat[c - 1][d] != '_')) or ((c != (longitud - 1) and c != 0) and ((mat[c + 1][d]) != '_' and (mat[c - 1][d]) != '_'))) and (((d == 0) and (mat[c][longitud - 1] != '_' and mat[c][d + 1] != '_')) or ((d == (longitud - 1)) and (mat[c][0] != '_' and mat[c][d - 1] != '_')) or ((d != (longitud - 1) and d != 0) and (mat[c][d + 1] != '_' and mat[c][d - 1] != '_'))):
        jugadores = ''
        system('cls')
        tablero()
        print('El ganador es', jugador,'\n')
        repetir = str(input('¿Desea jugar otra vez?: '))
        while repetir != 'si' and repetir != 'no':
            repetir = str(input('Error, ingrese si o no: '))
system('color F0')
repetir = 'si'
print('Bienvenido a Snake in action.\nPresione cualquier tecla para comenzar a jugar.')
system("pause>null")
system('cls')
instrucciones = str(input('Desea ver las instrucciones?: '))
while instrucciones != 'si' and instrucciones != 'no':
    instrucciones = str(input('Error, ingrese si o no: '))
if instrucciones == 'si':
    system('cls')
    print('Instrucciones:\n1.Antes de iniciar el juego, el jugador deberá elegir el tamaño del tablero.\n2.Existen dos jugadores, uno controlado por el usuario y el segundo puede ser controlado por el PC, si así lo desea.\n3.Se juega por turnos, donde cada jugador deberá hacer crecer a su serpiente hacia arriba, abajo, izquierda o derecha.\4La serpiente puede crecer saliéndose de una orilla del tablero y llegue a su correspondiente posición opuesta(movimiento espejo).\n5.Ganará el jugador que deje sin movimientos a su oponente.\n6.El primer jugador usa el símbolo B para la cabeza y b para el cuerpo.\n7.El segundo jugador usará el símbolo N para la cabeza de la serpiente y n para el cuerpo.\n\nPresione cualquier tecla para continuar.')
    system('pause>null')
while repetir == 'si':
    repetir = ''
    system('cls')
    jugadores = str(input('Desea jugar contra otro jugador?: '))
    while jugadores != 'si' and jugadores != 'no':
        jugadores = str(input('Error, ingrese si o no: '))
    while True:
        try:
            system('cls')
            longitud = int(input('Ingrese la longitud de los lados del tablero: '))
            while longitud < 4 or longitud > 12:
                system('cls')
                longitud = int(input('Error, ingrese una longitud válida: '))
            break
        except ValueError:
            pass
    turnos = random.randrange(2)
    mat = [[] for x in range (longitud)]
    for x in range (longitud):
        for y in range (longitud):
            mat[x].append('_')
    a = random.randrange(longitud)
    b = random.randrange(longitud)
    c = random.randrange(longitud)
    d = random.randrange(longitud)
    while c == a and d == b:
        c = random.randrange(longitud)
        d = random.randrange(longitud)
    if turnos == 0:
        mat[a][b] = 'B'
        mat[c][d] = 'N'
    else:
        mat[a][b] = 'N'
        mat[c][d] = 'B'
    system('cls')
    tablero()
    if turnos == 0:
        while True:
            validar_jugador('N')
            if repetir == 'si' or repetir == 'no':
                break
            if jugadores == 'no':
                print ('Su turno, B\n')
            elif jugadores == 'si':
                print ('Turno de B\n')
            turnos_jugador('b', 'B')
            validar_jugador('N')
            if repetir == 'si' or repetir == 'no':
                break
            system('cls')
            tablero()
            validar_jugador2('B')
            if repetir == 'si' or repetir == 'no':
                break
            if jugadores == 'no':
                print ('Turno del pc\n')
            elif jugadores == 'si':
                print ('Turno de N\n')
            turnos_jugador2('n', 'N')
            if jugadores == 'si':
                system('cls')
            tablero()
            validar_jugador2('B')
            if repetir == 'si' or repetir == 'no':
                break
    else:
        while True:
            validar_jugador2('N')
            if repetir == 'si' or repetir == 'no':
                break
            if jugadores == 'no':
                print ('Turno del pc\n')
            elif jugadores == 'si':
                print ('Turno de B\n')
            turnos_jugador2('b', 'B')
            validar_jugador2('N')
            if repetir == 'si' or repetir == 'no':
                break
            if jugadores == 'si':
                system('cls')
            tablero()
            validar_jugador('B')
            if repetir == 'si' or repetir == 'no':
                break
            if jugadores == 'no':
                print ('Su turno, N\n')
            elif jugadores == 'si':
                print ('Turno de N\n')
            turnos_jugador('n', 'N')
            system('cls')
            tablero()
            validar_jugador('B')
            if repetir == 'si' or repetir == 'no':
                break
system('cls')
print ('Presione cualquier tecla para salir.')
system("pause>null")
