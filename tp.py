"""TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""


def presentacion_info():
    print("¡Bienvenidos al Escape Room!")
    print("En este juego, deberan escapar de la universidad UADE, en la cual estan encerrados, tratando de escapar de las diferentes salas para encontrar la salida")
    print("Trabajen en equipo y utilicen su ingenio para encontrar pistas y desbloquear la salida.")
    print("Al comienzo deberas loguearte con tu usuario y contraseña.")
    print("¡Buena suerte!")
    
usuario = "jugador"
contraseña = "bruno"
desplazamiento = 3

def encriptar(texto, desplazamiento):
    resultado = ""
    for letra in texto:
        codigo = ord(letra)
        nuevo_codigo = (codigo - 32 + desplazamiento) % 95 + 32
        resultado = resultado + chr(nuevo_codigo)
        
    return resultado



def login():
    contador = 0
    while contador < 3:
        u = input("Ingrese su usuario: ")
        c = input("Ingrese su contraseña: ")
        if u == usuario and c == contraseña:
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
    print("3. ¡No se rindan! La salida es mas facil de lo que parece, usen su imaginacion e inteligencia!.")
    n = input("Ingrese 'volver' para volver al menu principal: ").lower()
    while n != "volver":
        print("Opcion invalida, ingrese nuevamente")
        n = input("Ingrese 'volver' para volver al menu principal: ").lower()
    menu()

def menu():
    print("MENU PRINCIPAL\n1- Instrucciones\n2- Jugar|\n3- Cambiar contraseña\n4- Cerrar sesion\nIngrese el numero segun la opcion que quiera realizar")
    opcion = int(input("Ingrese su opcion: "))
    while opcion > 4 or opcion < 1:
        print("Opcion invalida, ingrese nuevamente")
        opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        instrucciones()
    
presentacion_info()
encriptacion = encriptar(contraseña, desplazamiento)
print(encriptacion)
login() 
menu()