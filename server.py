import socket
import threading
import os
from colorama import Fore
from datetime import datetime

os.system("cls")

# Dirección IP y puerto en el que se escucharán las conexiones entrantes
direccion_ip = "127.0.0.1"
puerto = 12345

# Función que maneja cada conexión entrante
def manejar_cliente(cliente_socket, direccion):
    # Mensaje de entrada cuando se establece la conexión
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"-",Fore.GREEN,f"Conexión entrante desde {direccion[0]}:{direccion[1]}",Fore.WHITE)
    
    # Mensaje de bienvenida
    mensaje_bienvenida = "¡Conexion exitosa!"
    cliente_socket.send(mensaje_bienvenida.encode("utf-8"))

    # Bucle principal que recibe y envía mensajes hasta que el cliente cierra la conexión
    while True:
        # Recibimos datos del cliente y los decodificamos en una cadena de texto utilizando la codificación UTF-8
        datos = cliente_socket.recv(1024).decode("utf-8")
        if not datos:
            # Si no hay datos, significa que el cliente cerró la conexión
            break
        match datos:
            case "1":
                respuesta = "Solicitud 1"
            case "2":
                respuesta = "Solicitud 2"
            case _:
                respuesta = "No se como llegaste aca"

        # Generamos una respuesta codificada en UTF-8
        cliente_socket.send(respuesta.encode("utf-8"))
    
    # Mensaje de salida cuando se cierra la conexión
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),"-",Fore.RED,f"Conexión cerrada con {direccion[0]}:{direccion[1]}",Fore.WHITE)
    cliente_socket.close()

# Creamos un socket para el servidor utilizando IPv4 y TCP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket a la dirección IP y puerto especificados
servidor_socket.bind((direccion_ip, puerto))

# Ponemos el socket en modo de escucha
servidor_socket.listen()

# Mensaje de inicio del servidor
print(f"Servidor en escucha en {direccion_ip}:{puerto}")

# Bucle principal que acepta conexiones entrantes y crea un hilo para manejar cada una
while True:
    cliente_socket, direccion = servidor_socket.accept()
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
    hilo_cliente.start()
