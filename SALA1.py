"""SALA 1 DE AHORCADO"""

import random

PALABRAS = ["INGENIERIA", "FACULTAD", "INDEPENDENCIA", "LABORATORIOS", "PROGRAMACION", "MATERIAS", "EMPRESA", "CURSADA", "RECUPERATORIO", "CARRERA"]

INTENTOS_MAXIMOS = 6

def elegir_palabra():
    return random.choice(PALABRAS)

def pedir_letra(letras_usadas):
    while True:
        letra = input("Ingrese una letra: ").strip().upper()
        if len(letra) == 1 and letra.isalpha(): #verifica que sea una sola letra y sea una letra del abeecedario
            if letra not in letras_usadas: #si no uso la letra, la retorns
                return letra
            else:
                print("Ya ha ingresado esa letra. Intente nuevamente.") #en el caso de que se haya usado, la vuelve a pedir
        else:
            print("Texto invalido. Ingrese una sola letra del abecedario.") #si el texto no esuna sola letra, vuelve a pedir la letra

def mostrar_incognitas(palabra, letras_adivinadas):
    """Devuelve la palabra mostrando las letras adivinadas y '_' en las que faltan."""
    resultado = ""
    for letra in palabra: #recorro cada letra de la palabra
        if letra in letras_adivinadas: #en cada vuelta pregunto si la letra esta en las letras adivinadas, si es asi, la agrego al resultado, sino, agrego un guion bajo.
            resultado = resultado + letra + " " #si la adivino, agrego la letra y un espacio para que se vea mejor
        else:
            resultado = resultado + "_ " #No la adivino, se agrega un guion bajo y un espacio para que se vea mejor
    return resultado

def palabra_adivinada(palabra, letras_adivinadas):
    """Lo que hace esta funcuion es recorrer letra x letra la palabra incognita.
    Hay una condicion que verifica que la letra no este en la lista de las letras adivinadas. En ese caso, retorna False ya que quedan letras por descubrir.
    En el caso de que no queden letras por descubir, no entra en el if, ya que todas las letras de la palabra estan adivinadas."""
    for letra in palabra: 
        if letra not in letras_adivinadas: 
            return False 
    return True


def jugar_sala1():
    """Funcion principal de la sala 1. Se encarga de manejar el juego del ahorcado."""
    palabra = elegir_palabra()
    letras_adivinadas = []
    letras_usadas = []
    vidas = INTENTOS_MAXIMOS
    print("Bienvenido a la sala 1. Estas encerrado en el aula de Programacion, las puertas estan cerradas y debes acceder al sistema para abrirlas. Para lograrlo, tenes que adivinar la palabra secreta. Tenes 6 intentos para adivinarla. ¡Buena suerte!")
    while vidas > 0 and palabra_adivinada(palabra, letras_adivinadas) == False:
        print("\n" + mostrar_incognitas(palabra, letras_adivinadas))
        print("Vidas:", vidas)
        print("Letras usadas:", letras_usadas)

        letra = pedir_letra(letras_usadas)
        letras_usadas.append(letra)

        if letra in palabra:
            letras_adivinadas.append(letra)
            print("Bien! la letra", letra, "esta en la palabra")
        else:
            vidas = vidas - 1
            print("La letra", letra, "no esta. Perdiste una vida.")

    if palabra_adivinada(palabra, letras_adivinadas) == True:
        print("GANASTE! La palabra era:", palabra)
        return True
    else:
        print("PERDISTE. Te quedaste sin vidas. La palabra era:", palabra)
        return False
