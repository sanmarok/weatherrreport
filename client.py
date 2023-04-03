import os
import socket
import rich
from rich.table import Table
from colorama import Fore
from datetime import datetime, timedelta

def control_configuracion():
    os.system("cls")
    menu = Table("Opcion","Descripcion")
    menu.add_row("  1  ","   Local ")
    menu.add_row("  2  ","    LAN  ")
    rich.print(menu)
    
    opcion = int(input("Opcion: "))
    
    if opcion != 1 and opcion != 2:
        control_configuracion()
    else:
        match opcion:
            case 1:
                return "127.0.0.1"
            case 2:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                return ip_address
            case _:
                control_configuracion()


def mensajecontrol():
    mensaje = input("Opcion: ")
    if mensaje != "1" and mensaje != "2" and mensaje != "3" and mensaje != "4":
        os.system("cls")
        print(Fore.RED,"¡Error!",Fore.WHITE)
        rich.print(menu)
        mensajecontrol()
    else:
        return mensaje

os.system("cls")

# Dirección IP y puerto del servidor al que nos queremos conectar
direccion_ip = control_configuracion()
puerto = 12345

os.system("cls")
# Creamos un socket para el cliente utilizando IPv4 y TCP
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos el socket al servidor
cliente_socket.connect((direccion_ip, puerto))

# Recibimos el mensaje de bienvenida del servidor y lo decodificamos en una cadena de texto utilizando la codificación UTF-8
mensaje_bienvenida = cliente_socket.recv(1024).decode("utf-8")
print(Fore.GREEN, mensaje_bienvenida, Fore.WHITE)

menu = Table("Opcion","     Descripcion")
menu.add_row("  1  ","Temperatura")
menu.add_row("  2  ","Humedad")
menu.add_row("  3  ","Temperatura y humedad")
menu.add_row("  4  ","Cerrar sesion")
rich.print(menu)


# Bucle principal que permite al usuario enviar mensajes al servidor
while True:
    mensaje = mensajecontrol()
    
    # Si el usuario ingresa la opcion 4, salimos del bucle
    if mensaje == "4":
        break
    
    # Codificamos el mensaje en UTF-8 y lo enviamos al servidor
    cliente_socket.send(mensaje.encode("utf-8"))
    # Recibimos la respuesta del servidor y la decodificamos en una cadena de texto utilizando la codificación UTF-8
    respuesta = cliente_socket.recv(1024).decode("utf-8")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",f"Respuesta del servidor: {respuesta}")


# Cerramos la conexión con el servidor
cliente_socket.close()


