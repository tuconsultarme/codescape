"""TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""


def presentacion_info():
    print("¡Bienvenidos al Escape Room!")
    print("En este juego, deberan escapar de la universidad UADE, en la cual estan encerrados, tratando de escapar de las diferentes salas para encontrar la salida")
    print("Trabajen en equipo y utilicen su ingenio para encontrar pistas y desbloquear la salida.")
    print("Al comienzo deberas loguearte con tu usuario y contraseña.")
    print("¡Buena suerte!")

USUARIO = "jugador"
CONTRASEÑA = "bruno"
DESPLAZAMIENTO = 3

def encriptar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        codigo = ord(letra)
        nuevo_codigo = (codigo - 32 + desplazamiento) % 95 + 32
        resultado = resultado + chr(nuevo_codigo)

    return resultado



def validar_credenciales(usuario_ingresado, contraseña_ingresada, usuario_correcto, contraseña_correcta):
    """Tiene como parametro el usuario y la contraseña ingresados por el usuario, y los compara con los correctos."""
    if usuario_ingresado == usuario_correcto and contraseña_ingresada == contraseña_correcta:
        return True
    else:
        return False


def login(usuario_correcto, contraseña_correcta):
    """Solicita al usuario que ingrese su usuario y contraseña con un limite maximo de 3 intentos erroneos.
    La funcion recibe como parametro el usuario y contraseña correcta para la comparacion.
    Termina el programa si se agotan los intentos.
    """
    contador = 0
    while contador < 3:
        usuario_ingresado = input("Ingrese su usuario: ").strip()
        contraseña_ingresada = input("Ingrese su contraseña: ").strip()
        if validar_credenciales(usuario_ingresado, contraseña_ingresada, usuario_correcto, contraseña_correcta):
            print("ACCESO CONCEDIDO, BIENVENIDO!.")
            return
        contador += 1
        if contador < 3:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
    print("Ha superado el limite de intentos. El juego se cerrará.")
    exit()

def instrucciones():
    print("INSTRUCCIONES DEL JUEGO")
    print("1. Deben trabajar en equipo para resolver las salas y desbloquear la salida.")
    print("2. Cada sala tiene un juego el cual deben resolver.")
    print("3. ¡No se rindan! La salida es mas facil de lo que parece, usen su imaginacion e inteligencia!")
    opcion_volver = input("Ingrese 'volver' para volver al menu principal: ").lower()
    while opcion_volver != "volver":
        print("Opcion invalida, ingrese nuevamente")
        opcion_volver = input("Ingrese 'volver' para volver al menu principal: ").lower().strip()
    menu()

def menu():
    print("MENU PRINCIPAL\n1- Instrucciones\n2- Jugar\n3- Cambiar contraseña\n4- Cerrar sesion\nIngrese el numero segun la opcion que quiera realizar")
    opcion_menu = int(input("Ingrese su opcion: "))
    while opcion_menu > 4 or opcion_menu < 1:
        print("Opcion invalida, ingrese nuevamente")
        opcion_menu = int(input("Ingrese su opcion: "))
    if opcion_menu == 1:
        instrucciones()

presentacion_info()
encriptacion = encriptar(CONTRASEÑA, DESPLAZAMIENTO)
print(encriptacion)
login(USUARIO, CONTRASEÑA)
menu()
