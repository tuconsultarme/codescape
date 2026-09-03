"""TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""


def presentacion_info():
    print("¡Bienvenidos al Escape Room!")
    print("En este juego, deberan escapar de la universidad UADE, en la cual estan encerrados, tratando de escapar de las diferentes salas para encontrar la salida")
    print("Trabajen en equipo y utilicen su ingenio para encontrar pistas y desbloquear la salida.")
    print("Al comienzo deberas loguearte con tu usuario y contraseña.")
    print("¡Buena suerte!")
    
usuario = "jugador"
contrasena = "bruno"
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
        if u == usuario and c == contrasena:
            print("ACCESO CONCEDIDO, BIENVENIDO!.")
            return
        contador += 1
        if contador < 3:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
    print("Ha superado el límite de intentos. El juego se cerrará.")
    exit()

presentacion_info()
encriptacion = encriptar(contrasena, desplazamiento)
print(encriptacion)
login()