import socket
import os

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
print(mensaje_bienvenida)

# Bucle principal que permite al usuario enviar mensajes al servidor
while True:
    mensaje = input("Ingrese un mensaje para enviar al servidor: ")
    # Codificamos el mensaje en UTF-8 y lo enviamos al servidor
    cliente_socket.send(mensaje.encode("utf-8"))
    # Recibimos la respuesta del servidor y la decodificamos en una cadena de texto utilizando la codificación UTF-8
    respuesta = cliente_socket.recv(1024).decode("utf-8")
    print(f"Respuesta del servidor: {respuesta}")
    # Si el usuario ingresa la palabra "adios", salimos del bucle
    if mensaje.lower() == "adios":
        break

# Cerramos la conexión con el servidor
cliente_socket.close()


