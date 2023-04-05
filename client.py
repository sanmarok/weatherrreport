import os
import importlib

def verificar_instalacion_librerias(libs):
    """
    Verifica si las librerías están instaladas y las instala si es necesario.

    Args:
        libs (list): Lista de nombres de las librerías a verificar.

    Returns:
        None
    """
    for lib in libs:
        try:
            importlib.import_module(lib)
            print(f"{lib} está instalada.")
        except ImportError:
            print(f"{lib} no está instalada. Instalando...")
            os.system(f"pip install {lib}")
            print(f"{lib} ha sido instalada.")
            
# Lista de librerías a verificar
libs = ["os", "socket", "rich", "ast", "rich.table", "colorama", "datetime"]

# Verificar e instalar las librerías necesarias
verificar_instalacion_librerias(libs)
           
import socket
import rich
import ast
from rich.table import Table
from colorama import Fore
from datetime import datetime

dict_data_local = {'temperatura': "", 'humedad': ""}

def control_configuracion():
    os.system("cls")
    menu = Table("Opcion","Descripcion")
    menu.add_row("  1  ","   Local ")
    menu.add_row("  2  ","    LAN  ")
    rich.print(menu)
    
    opcion = int(input("\nOpcion: "))
    
    while opcion != 1 and opcion != 2:
        os.system("cls")
        print(Fore.RED,"¡Error!",Fore.WHITE)
        rich.print(menu)
        opcion = int(input("\nOpcion: "))        

    match opcion:
        case 1:
            return "127.0.0.1"
        case 2:
            ip_address = str(input("Ingrese la IP del servidor:"))
            return ip_address


def mensajecontrol():
    mensaje = input("\nOpcion: ")
    while mensaje != "1" and mensaje != "2" and mensaje != "3" and mensaje != "4":
        os.system("cls")
        print(Fore.RED,"¡Error!",Fore.WHITE)
        rich.print(menu)
        mensaje = input("\nOpcion: ")

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
print(Fore.GREEN,"\t",mensaje_bienvenida, Fore.WHITE,"\n")

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
    if(mensaje != "4"):
        cliente_socket.send(mensaje.encode("utf-8"))
        # Recibimos la respuesta del servidor y la decodificamos en una cadena de texto utilizando la codificación UTF-8
        respuesta = cliente_socket.recv(1024).decode("utf-8")
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",f" Respuesta del servidor: {respuesta}")
        dict_data = ast.literal_eval((str(respuesta)))
        
    match mensaje:
        case "1":
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.BLUE,f"Temperatura actualizada",Fore.WHITE)
            dict_data_local["temperatura"] = dict_data["temperatura"]
            print("La temperatura es",dict_data_local["temperatura"],"C° y la humedad exterior es",dict_data_local["humedad"],"%")
        case "2":
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.BLUE,f"Humedad actualizada",Fore.WHITE)
            dict_data_local["humedad"] = dict_data["humedad"]
            print("La temperatura es",dict_data_local["temperatura"],"C° y la humedad exterior es",dict_data_local["humedad"],"%")
        case "3":
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.BLUE,f"Medicion actualizada",Fore.WHITE)
            dict_data_local["temperatura"] = dict_data["temperatura"]
            dict_data_local["humedad"] = dict_data["humedad"]
            print("La temperatura es",dict_data_local["temperatura"],"C° y la humedad exterior es",dict_data_local["humedad"],"%")
        case "4":
            # Si el usuario ingresa la opcion 4, salimos del bucle
            break
        case _:
            print("¡Felicidades! Encontr4e un error")
    
# Cerramos la conexión con el servidor
cliente_socket.close()


