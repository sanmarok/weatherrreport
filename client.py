import socket
import os
import rich
from rich.table import Table
from colorama import Fore


def mensajecontrol():
    mensaje = input("\nOpcion: ")
    if mensaje != "1" and mensaje != "2" and mensaje != "3" and mensaje != "4":
        os.system("cls")
        print(Fore.RED,"¡Error!",Fore.WHITE)
        rich.print(menu)
        mensajecontrol()
    else:
        return mensaje

os.system("cls")
# Dirección IP y puerto del servidor al que nos queremos conectar
direccion_ip = "127.0.0.1"
puerto = 12345

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
    # Codificamos el mensaje en UTF-8 y lo enviamos al servidor
    cliente_socket.send(mensaje.encode("utf-8"))
    # Recibimos la respuesta del servidor y la decodificamos en una cadena de texto utilizando la codificación UTF-8
    respuesta = cliente_socket.recv(1024).decode("utf-8")
    print(f"Respuesta del servidor: {respuesta}")
    # Si el usuario ingresa la palabra "adios", salimos del bucle
    if mensaje == "4":
        break

# Cerramos la conexión con el servidor
cliente_socket.close()


