"""SALA 2 - MINI BATALLA NAVAL
TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""

import random

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

def mostrar_tablero(tablero):
    """Muestra el tablero en pantalla con los numeros de fila y de columna."""
    print("  1 2 3 4") #numeros de las columnas

    numero_fila = 1
    for fila in tablero: #ciclo en las filas, que son listas
        print(numero_fila, fila[0], fila[1], fila[2], fila[3])
        numero_fila = numero_fila + 1 #suma uno para que los numeros de las listas vayan avanzando

def posicion_libre(barcos, fila, columna):
    """Devuelve True si (fila, columna) no esta pegada a ningun barco ya puesto.
    Se considera pegado si la distancia en filas y en columnas es 1 o menos
    (eso cubre horizontal, vertical, diagonal y el mismo lugar)."""
    for barco in barcos:
        fila_barco = barco[0] #agarra el primer elemento de la coordenada del barco, que es la fila
        columna_barco = barco[1] #agarra el segundo elemento de la coordenada del barco, que es la columna
        distancia_filas = abs(fila - fila_barco) #abs te da un valor absoluto, osea aunque la resta de negativa te da el resultado positivo. Esto es para que no importe si la resta es negativa o positiva, solo importa la distancia.
        distancia_columnas = abs(columna - columna_barco)
        if distancia_filas <= 1 and distancia_columnas <= 1: #para que no este pegado, la distancia en filas y columnas tiene que ser mayor a 1. Si es menor o igual a 1, esta pegado.
            return False
    return True


def generar_barcos():
    """Genera una lista con las coordenadas de los barcos.
    Devuelve una lista de coordenadas (fila, columna) con la cantidad de barcos especificada en la variable de cantidad de barcos."""
    barcos = []
    while len(barcos) < CANTIDAD_BARCOS: #mientras que los barcos sean menores a 3, va a seguir generando coordenadas
        fila = random.randint(0, FILAS - 1) #porq las filas van de 0 a 3
        columna = random.randint(0, COLUMNAS - 1)
        if posicion_libre(barcos, fila, columna): #no repetida y no pegada a otro barco
            barcos.append((fila, columna))
    return barcos


def pedir_coordenada(texto, maximo):
    """Pide un numero entre 1 y 4 y no lo devuelve hasta que sea valido.
    Devuelve el numero menos 1, para poder usarlo como indice de la lista."""
    while True:
        valor = input(texto)
        if valor.isdigit() == False: #si no es un numero, vuelve a pedir
            print("Tenes que ingresar un numero.")
        else:
            valor = int(valor)
            if valor < 1 or valor > maximo:#si esta fuera del tablero, vuelve a pedir
                print("El numero tiene que estar entre 1 y", maximo)
            else:
                return valor - 1 #el jugador escribe 1-4, la lista usa 0-3

def jugar_sala2():
    """Funcion principal de la sala 2. Se encarga de manejar el juego de batalla naval.
    Devuelve True si el jugador hunde todos los barcos, False si se queda sin intentos."""
    print("Pudiste pasar la primera prueba del aula de programacion, lo unico que te falta ahora es poder abrir la puerta de salida. Resolve esta batalla naval para poder salir de la facultad! ¡Buena suerte!")

    tablero = crear_tablero() 
    barcos = generar_barcos()
    errores = 0
    aciertos = 0

    while errores < ERRORES_MAXIMOS and aciertos < CANTIDAD_BARCOS:
        mostrar_tablero(tablero)
        print("Errores:", errores, "de", ERRORES_MAXIMOS,"\n" "Barcos hundidos:", aciertos, "de", CANTIDAD_BARCOS)

        fila = pedir_coordenada("Ingrese la fila (1 a 4): ", FILAS)
        columna = pedir_coordenada("Ingrese la columna (1 a 4): ", COLUMNAS)

        if tablero[fila][columna] != SIN_EXPLORAR:# ya disparo ahi
            print("Ya disparaste a esa posicion. Elegi otra.")
        elif (fila, columna) in barcos: #le pego a un barco, suma acierto
            tablero[fila][columna] = IMPACTO
            aciertos = aciertos + 1
            print("IMPACTO! Le pegaste a un barco.")
        else: #agua
            tablero[fila][columna] = AGUA
            errores = errores + 1
            print("Agua. Fallaste el disparo.")

    mostrar_tablero(tablero)
    if aciertos == CANTIDAD_BARCOS:
        print("GANASTE! Hundiste todos los barcos y la puerta se abre. Muchas Gracias por jugar!")
        return True
    else:
        print("PERDISTE. Te quedaste sin intentos y no pudiste salir.")
        return False



