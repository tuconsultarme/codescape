"""TRABAJO GRUPAL ESCAPE ROOM
GRUPO: BAUTISTA KAHR, BRUNO MASSACCESI, SALVADOR SONCINI, VALENTINA PERIE"""


def presentacion_info():
    print("¡Bienvenidos al Escape Room!")
    print("En este juego, deberan escapar de la universidad UADE, en la cual estan encerrados, tratando de escapar ya que se quedaron dormidos en el aula de la clase de Programacion! Explora la facultad para poder salir!")
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



def validar_credenciales(usuario_ingresado, contraseña_ingresada, usuario_correcto, contraseña_correcta): #lapodemos reutilizar
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


def pedir_opcion(): #La hice porque el programa rompia cuando se ingresaba un texto en vez de un numero en la parte de elegir la opcion del menu. Ahora con esto no se rompe y verifica el tipo de texto y el rango
    """Pide una opcion del menu y no la devuelve hasta que sea un numero valido entre 1 y 4.
    Ademas verifica que el texto ingresado sea un numero y no un texto.
    En el caso de ser un numero, lo convierte a int
    Sino, vuelve a pedir la opcion hasta que sea valida."""
    while True:
        opcion_menu = input("Ingrese su opcion: ")
        while opcion_menu.isdigit() == False: #si no es digito, vuelve a pedir la opcion
            print("Opcion invalida, ingrese nuevamente")
            opcion_menu = input("Ingrese su opcion: ")
        opcion_menu = int(opcion_menu) #lo comvertimos a integer para poder comparar el rango
        if opcion_menu > 4 or opcion_menu < 1:
            print("Opcion invalida, ingrese nuevamente")
        else:
            return opcion_menu


def menu(usuario, contraseña):
    """Bucle de menu para elegir la opcion que desea el usuario.
    Utiliza usuario y contraseña como parametros para poder cambiar la contraseña si asi lo elije.
    """
    while True: #puse el while true porq si elegia la opcion 1 y volvia al menu la funcion se terminaba, podias hacer una sola cosa. Ahora la unica forma de que termine el bucle es cerrando sesion o eligiendo el juego, que no lo hice todavia.
        print("MENU PRINCIPAL\n1- Instrucciones\n2- Jugar\n3- Cambiar contraseña\n4- Cerrar sesion\nIngrese el numero segun la opcion que quiera realizar")
        opcion_menu = pedir_opcion() 
        if opcion_menu == 1:
            instrucciones()
        elif opcion_menu == 2:
            print("")
        elif opcion_menu == 3:
            contraseña = cambiar_contraseña(usuario, contraseña)
        elif opcion_menu == 4:
            cerrar_sesion()
            login(usuario, contraseña)
            menu(usuario, contraseña)
            break


def cerrar_sesion():
    """Opcion de cerrar sesion la cual vuelve al login."""
    print("Sesion cerrada con exito. Nos vemos")

def cambiar_contraseña(usuario_correcto, contraseña_correcta):
    """Pide los datos actuales y devuelve la contraseña que queda actualemente.

    Si valida bien, devuelve la nueva. En el otro caso, devuelve la actual sin cambios.
    
    Da como parametros el usuario y la contraseña correctos para poder validar los datos ingresados por el usuario.
    """
    usuario_actual = input("Ingrese su usuario actual: ").strip()
    contraseña_actual = input("Ingrese su contraseña actual: ").strip()
    if validar_credenciales(usuario_actual, contraseña_actual, usuario_correcto, contraseña_correcta): #reutilizamps la funcion
        nueva_contraseña = input("Ingrese su nueva contraseña: ").strip()
        print("Contraseña cambiada con exito.")
        encriptacion_nueva = encriptar(nueva_contraseña, DESPLAZAMIENTO) #usamos la funcion de encriptar para encriptar la nueva contraseña
        print("La nueva contraseña encriptada es:", encriptacion_nueva)
        return nueva_contraseña #retorna la nueva contraseña
    print("Usuario o contraseña incorrectos. No se pudo cambiar la contraseña.")
    return contraseña_correcta #retorna la contraseña actual sin cambios


presentacion_info()
encriptacion = encriptar(CONTRASEÑA, DESPLAZAMIENTO)
print("La contraseña encriptada es: ", encriptacion)
login(USUARIO, CONTRASEÑA)
menu(USUARIO, CONTRASEÑA)