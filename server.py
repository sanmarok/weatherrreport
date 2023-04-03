import os
import socket
import threading
import rich
import requests
from colorama import Fore
from datetime import datetime, timedelta
from rich.table import Table

class WeatherData:
    def __init__(self, date, time, temp, hi, low, out_hum, dew_pt, wind_speed, wind_dir, wind_run, hi_speed, hi_dir, wind_chill, heat_index, thw_index, thsw_index, rain, rain_rate, solar_rad, solar_energy, hi_solar_rad, solar_heat_index, uv_index, uv_dose, in_temp, in_hum, in_dew, in_heat, in_emc, in_density, et, wind_samp, wind_tx, iss_recept, arc_int):
        self.date = date
        self.time = time
        self.temp = temp
        self.hi = hi
        self.low = low
        self.out_hum = out_hum
        self.dew_pt = dew_pt
        self.wind_speed = wind_speed
        self.wind_dir = wind_dir
        self.wind_run = wind_run
        self.hi_speed = hi_speed
        self.hi_dir = hi_dir
        self.wind_chill = wind_chill
        self.heat_index = heat_index
        self.thw_index = thw_index
        self.thsw_index = thsw_index
        self.rain = rain
        self.rain_rate = rain_rate
        self.solar_rad = solar_rad
        self.solar_energy = solar_energy
        self.hi_solar_rad = hi_solar_rad
        self.solar_heat_index = solar_heat_index
        self.uv_index = uv_index
        self.uv_dose = uv_dose
        self.in_temp = in_temp
        self.in_hum = in_hum
        self.in_dew = in_dew
        self.in_heat = in_heat
        self.in_emc = in_emc
        self.in_density = in_density
        self.et = et
        self.wind_samp = wind_samp
        self.wind_tx = wind_tx
        self.iss_recept = iss_recept
        self.arc_int = arc_int

# Función que maneja cada conexión entrante
def manejar_cliente(cliente_socket, direccion):
    
    #Variable globales
    global last_update_g
    global data_measurement_g
    # Mensaje de entrada cuando se establece la conexión
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.GREEN,f"Conexión entrante desde    ",Fore.WHITE,f"{direccion[0]}:{direccion[1]}")
    
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
                if(datetime.now() - last_update_g >= timedelta(minutes= 5)):
                    data_measurement_g = weather_measurement()
                    last_update_g = datetime.now()
                    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.BLUE,f"Medicion actualizada",Fore.WHITE)
                
                respuesta = f"Temperatura: {data_measurement_g.temp}C° - Humedad: {data_measurement_g.out_hum}%"
                # Generamos una respuesta codificada en UTF-8
                cliente_socket.send(respuesta.encode("utf-8"))
                print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.YELLOW,f"Solicitud tipo 1 entregada ",Fore.WHITE,f"{direccion[0]}:{direccion[1]}")
            case "2":
                respuesta = "Solicitud 2"
            case _:
                respuesta = "No se como llegaste aca"

    # Mensaje de salida cuando se cierra la conexión
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.RED,f"Conexión cerrada con       ",Fore.WHITE,f"{direccion[0]}:{direccion[1]}")
    cliente_socket.close()
    
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
          
def weather_measurement():
    url = "https://www.frcon.utn.edu.ar/galileo/downld02.txt"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        lastjump = response.text.rfind("\n")
        text = response.text[0:lastjump]
        prelastjum = text.rfind("\n")
        text = response.text[prelastjum+1:lastjump]
        
        values = text.split()
        
        weatherreport = WeatherData(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11], values[12], values[13], values[14], values[15], values[16], values[17], values[18], values[19], values[20], values[21], values[22], values[23], values[24], values[25], values[26], values[27], values[28], values[29], values[30], values[31], values[32], values[33], values[34])
        
        return weatherreport
    
    except requests.exceptions.RequestException:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.RED,f"ERROR SOLICITANDO DATOS",Fore.WHITE)
        weather_measurement()


os.system("cls")

# Dirección IP y puerto en el que se escucharán las conexiones entrantes
direccion_ip = control_configuracion()
puerto = 12345

os.system("cls")

# Creamos un socket para el servidor utilizando IPv4 y TCP
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazamos el socket a la dirección IP y puerto especificados
servidor_socket.bind((direccion_ip, puerto))

# Ponemos el socket en modo de escucha
servidor_socket.listen()

# Mensaje de inicio del servidor
print(f"\tServidor en escucha en {direccion_ip}:{puerto}\n")

data_measurement_g = weather_measurement()
last_update_g = datetime.now()

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")," -",Fore.BLUE,f"Medicion inicial tomada",Fore.WHITE)

# Bucle principal que acepta conexiones entrantes y crea un hilo para manejar cada una
while True:
    cliente_socket, direccion = servidor_socket.accept()
    hilo_cliente = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
    hilo_cliente.start()
