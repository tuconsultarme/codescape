"""SALA 1 - AHORCADO
TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""

from random import choice

PALABRAS_SECRETAS = ["PROGRAMACION", "BIBLIOTECA", "PROFESOR", "ASCENSOR",
                     "PIZARRON", "MOCHILA", "PARCIAL", "CAFETERIA",
                     "ESCALERA", "LABORATORIO", "ALGORITMO", "TECLADO"]
VIDAS_MAXIMAS = 6


def elegir_palabra(lista_de_palabras):
    """Elige una palabra al azar de la lista usando choice().
    Recibe como parametro la lista de palabras y devuelve una sola."""
    palabra_elegida = choice(lista_de_palabras)
    return palabra_elegida


def mostrar_casilleros(palabra_secreta, letras_descubiertas):
    """Dibuja un casillero por cada letra de la palabra y le pone la letra encima.
    Si la letra todavia no fue descubierta, el casillero queda vacio.
    Recibe la palabra secreta y las letras que el jugador ya descubrio."""
    fila_de_letras = ""
    fila_de_casilleros = ""
    for letra in palabra_secreta:
        if letra in letras_descubiertas:
            fila_de_letras = fila_de_letras + " " + letra + "  "
        else:
            fila_de_letras = fila_de_letras + "    "
        fila_de_casilleros = fila_de_casilleros + "___ "
    print(fila_de_letras)
    print(fila_de_casilleros)


def pedir_letra():
    """Pide una letra y no la devuelve hasta que sea valida.
    Verifica que se haya ingresado un solo caracter y que ese caracter sea una letra.
    Como no sale del bucle hasta que este bien, una entrada invalida no gasta vidas."""
    while True:
        letra_ingresada = input("Ingrese una letra: ").strip().upper()
        if len(letra_ingresada) != 1:
            print("Debe ingresar exactamente una letra.")
        elif letra_ingresada.isalpha() == False:
            print("Solo se permiten letras, no numeros ni simbolos.")
        else:
            return letra_ingresada


def esta_completa(palabra_secreta, letras_descubiertas):
    """Verifica si ya se descubrieron todas las letras de la palabra.
    Devuelve True si esta completa y False si todavia falta alguna."""
    for letra in palabra_secreta:
        if letra not in letras_descubiertas:
            return False
    return True


def separar_con_espacios(letras_usadas):
    """Devuelve las letras usadas separadas con espacios para que se lean mejor."""
    texto = ""
    for letra in letras_usadas:
        texto = texto + letra + " "
    return texto


def mostrar_estado(palabra_secreta, letras_descubiertas, letras_usadas, vidas_restantes):
    """Muestra los casilleros de la palabra, las letras ya usadas y las vidas que quedan."""
    print("")
    mostrar_casilleros(palabra_secreta, letras_descubiertas)
    print("Letras usadas:", separar_con_espacios(letras_usadas))
    print("Vidas:", vidas_restantes)


def jugar_sala1():
    """Sala 1 del Escape Room, el juego del Ahorcado.
    Elige una palabra al azar y el jugador la tiene que descubrir letra por letra.
    Arranca con 6 vidas y pierde una por cada letra que no este en la palabra.
    Devuelve True si el jugador supera la sala y False si se queda sin vidas."""
    palabra_secreta = elegir_palabra(PALABRAS_SECRETAS)
    letras_descubiertas = ""
    letras_usadas = ""
    vidas_restantes = VIDAS_MAXIMAS

    print("")
    print("SALA 1 - EL AULA DE PROGRAMACION")
    print("Te despertaste solo en el aula y la puerta esta cerrada con una clave.")
    print("Adivina la palabra oculta para poder salir. Tenes", VIDAS_MAXIMAS, "vidas.")

    while vidas_restantes > 0 and esta_completa(palabra_secreta, letras_descubiertas) == False:
        mostrar_estado(palabra_secreta, letras_descubiertas, letras_usadas, vidas_restantes)
        letra_ingresada = pedir_letra()
        if letra_ingresada in letras_usadas:  # si ya la uso no le sacamos una vida
            print("Esa letra ya la ingresaste antes. Probe con otra.")
        else:
            letras_usadas = letras_usadas + letra_ingresada
            if letra_ingresada in palabra_secreta:
                letras_descubiertas = letras_descubiertas + letra_ingresada
                print("MUY BIEN! La letra", letra_ingresada, "esta en la palabra.")
            else:
                vidas_restantes = vidas_restantes - 1
                if vidas_restantes == 1:
                    print("La letra", letra_ingresada, "no esta en la palabra. Te queda 1 vida.")
                else:
                    print("La letra", letra_ingresada, "no esta en la palabra. Te quedan", vidas_restantes, "vidas.")

    print("")
    if esta_completa(palabra_secreta, letras_descubiertas):
        mostrar_casilleros(palabra_secreta, letras_descubiertas)
        print("EXCELENTE! La palabra era", palabra_secreta)
        print("La puerta del aula se abrio, superaste la Sala 1.")
        return True
    else:
        print("Te quedaste sin vidas. La palabra era", palabra_secreta)
        print("No pudiste salir del aula. Perdiste el desafio.")
        return False
