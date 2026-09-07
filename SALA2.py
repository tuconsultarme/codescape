"""SALA 2 - MINI BATALLA NAVAL
TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""

from random import randint

FILAS = 4
COLUMNAS = 4
CANTIDAD_BARCOS = 3
ERRORES_MAXIMOS = 5

SIN_EXPLORAR = "~"
IMPACTO = "X"
AGUA = "O"


def crear_tablero():
    """Arma la matriz del tablero con todos los casilleros sin explorar.
    Devuelve una lista de listas de FILAS por COLUMNAS."""
    tablero = []
    for fila in range(FILAS):
        fila_nueva = []
        for columna in range(COLUMNAS):
            fila_nueva.append(SIN_EXPLORAR)
        tablero.append(fila_nueva)
    return tablero


def posicion_valida(barcos, fila, columna):
    """Verifica si se puede poner un barco nuevo en esa fila y columna.
    Recorre los barcos ya ubicados y mide la distancia en filas y en columnas.
    Si las dos distancias son menores o iguales a 1 los barcos quedarian juntos,
    y eso incluye el caso de que sea exactamente la misma posicion.
    Devuelve True si la posicion sirve y False si no."""
    for barco in barcos:
        fila_barco = barco[0]
        columna_barco = barco[1]
        distancia_filas = abs(fila - fila_barco)
        distancia_columnas = abs(columna - columna_barco)
        if distancia_filas <= 1 and distancia_columnas <= 1:
            return False
    return True


def generar_barcos():
    """Ubica los 3 barcos en posiciones al azar del tablero.
    Antes de guardar cada posicion la controla con posicion_valida(), asi
    ningun barco queda repetido ni pegado a otro en horizontal, vertical o diagonal.
    Si se traba porque no queda lugar libre, empieza de nuevo con el tablero vacio.
    Devuelve una lista con las posiciones de los barcos."""
    while True:
        barcos = []
        intentos = 0
        while len(barcos) < CANTIDAD_BARCOS and intentos < 300:
            fila = randint(0, FILAS - 1)
            columna = randint(0, COLUMNAS - 1)
            if posicion_valida(barcos, fila, columna):
                barcos.append([fila, columna])
            intentos = intentos + 1
        if len(barcos) == CANTIDAD_BARCOS:
            return barcos


def hay_barco(barcos, fila, columna):
    """Verifica si en esa fila y columna hay un barco escondido.
    Devuelve True si hay un barco y False si no hay nada."""
    for barco in barcos:
        if barco[0] == fila and barco[1] == columna:
            return True
    return False


def mostrar_tablero(tablero):
    """Dibuja el tablero en pantalla con los numeros de fila y de columna.
    Los barcos que todavia no fueron encontrados no se muestran."""
    encabezado = "    "
    for numero_columna in range(COLUMNAS):
        encabezado = encabezado + str(numero_columna + 1) + "   "
    print("")
    print(encabezado)
    for numero_fila in range(FILAS):
        linea = str(numero_fila + 1) + "   "
        for casillero in tablero[numero_fila]:
            linea = linea + casillero + "   "
        print(linea)


def mostrar_marcador(barcos_hundidos, errores_restantes):
    """Informa cuantos barcos hundio, cuantos le faltan y cuantos errores le quedan."""
    barcos_restantes = CANTIDAD_BARCOS - barcos_hundidos
    print("Barcos hundidos:", barcos_hundidos, "| Barcos restantes:", barcos_restantes, "| Errores disponibles:", errores_restantes)


def pedir_coordenada(texto, maximo):
    """Pide un numero de fila o de columna y no lo devuelve hasta que sea valido.
    Controla que se haya ingresado un numero y que ese numero exista en el tablero.
    Como no sale del bucle hasta que este bien, un ingreso invalido no gasta disparos.
    Devuelve el numero restandole 1, para poder usarlo como posicion de la matriz."""
    while True:
        valor_ingresado = input(texto).strip()
        if valor_ingresado.isdigit() == False:
            print("Debe ingresar un numero.")
        else:
            valor_ingresado = int(valor_ingresado)
            if valor_ingresado < 1 or valor_ingresado > maximo:
                print("El numero debe estar entre 1 y", maximo)
            else:
                return valor_ingresado - 1


def revelar_barcos(tablero, barcos):
    """Marca en el tablero donde estaban los barcos que no encontro.
    Se usa cuando el jugador pierde, para mostrarle la solucion."""
    for barco in barcos:
        fila = barco[0]
        columna = barco[1]
        if tablero[fila][columna] != IMPACTO:
            tablero[fila][columna] = IMPACTO
    return tablero


def jugar_sala2():
    """Sala 2 del Escape Room, la Mini Batalla Naval.
    Esconde 3 barcos en un tablero de 4x4 y el jugador tiene que encontrarlos.
    Arranca con 5 errores y pierde uno cada vez que dispara al agua.
    Devuelve True si hunde los 3 barcos y False si se queda sin errores."""
    tablero = crear_tablero()
    barcos = generar_barcos()
    barcos_hundidos = 0
    errores_restantes = ERRORES_MAXIMOS

    print("")
    print("SALA 2 - EL LABORATORIO INUNDADO")
    print("Saliste del aula pero el laboratorio se inundo y hay una flota bloqueando la salida.")
    print("Hundi los", CANTIDAD_BARCOS, "barcos escondidos en el tablero de", FILAS, "x", COLUMNAS, "para poder pasar.")
    print("Podes errar hasta", ERRORES_MAXIMOS, "disparos.")
    print("Referencias:", SIN_EXPLORAR, "sin explorar |", AGUA, "agua |", IMPACTO, "barco hundido")

    while errores_restantes > 0 and barcos_hundidos < CANTIDAD_BARCOS:
        mostrar_tablero(tablero)
        mostrar_marcador(barcos_hundidos, errores_restantes)
        fila = pedir_coordenada("Ingrese la fila (1 a " + str(FILAS) + "): ", FILAS)
        columna = pedir_coordenada("Ingrese la columna (1 a " + str(COLUMNAS) + "): ", COLUMNAS)

        if tablero[fila][columna] != SIN_EXPLORAR:  # ya disparo ahi, no le descontamos nada
            print("Esa posicion ya la atacaste antes. Elegi otra.")
        elif hay_barco(barcos, fila, columna):
            tablero[fila][columna] = IMPACTO
            barcos_hundidos = barcos_hundidos + 1
            print("¡IMPACTO! Barco hundido.")
            mostrar_marcador(barcos_hundidos, errores_restantes)
        else:
            tablero[fila][columna] = AGUA
            errores_restantes = errores_restantes - 1
            print("AGUA")
            if errores_restantes == 1:
                print("Te queda 1 error.")
            else:
                print("Te quedan", errores_restantes, "errores.")
            mostrar_marcador(barcos_hundidos, errores_restantes)

    if barcos_hundidos == CANTIDAD_BARCOS:
        mostrar_tablero(tablero)
        print("")
        print("EXCELENTE! Hundiste toda la flota.")
        print("El agua se drena y la puerta de salida queda libre. Superaste la Sala 2.")
        return True
    else:
        tablero = revelar_barcos(tablero, barcos)
        mostrar_tablero(tablero)
        print("")
        print("Te quedaste sin errores disponibles. Ahi estaban los barcos.")
        print("No pudiste cruzar el laboratorio. Perdiste el desafio.")
        return False
