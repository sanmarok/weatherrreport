import os
import requests
import json
from colorama import Fore
from datetime import datetime, timedelta

url = "https://www.frcon.utn.edu.ar/galileo/downld02.txt"
trys = 0

os.system("cls")

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

    def print_data(self):
        print("Fecha:                                           ", Fore.GREEN + self.date               + Fore.WHITE)
        print("Temperatura:                                     ", Fore.GREEN + self.temp               + Fore.WHITE)
        print("Hora:                                            ", Fore.GREEN + self.time               + Fore.WHITE)
        print("Temperatura máxima:                              ", Fore.GREEN + self.hi                 + Fore.WHITE)
        print("Temperatura mínima:                              ", Fore.GREEN + self.low                + Fore.WHITE)
        print("Humedad:                                         ", Fore.GREEN + self.out_hum            + Fore.WHITE)
        print("Punto de rocío:                                  ", Fore.GREEN + self.dew_pt             + Fore.WHITE)
        print("Velocidad del viento:                            ", Fore.GREEN + self.wind_speed         + Fore.WHITE)
        print("Dirección del viento:                            ", Fore.GREEN + self.wind_dir           + Fore.WHITE)
        print("Distancia recorrida por el viento:               ", Fore.GREEN + self.wind_run           + Fore.WHITE)
        print("Velocidad máxima del viento:                     ", Fore.GREEN + self.hi_speed           + Fore.WHITE)
        print("Dirección de la velocidad máxima del viento:     ", Fore.GREEN + self.hi_dir             + Fore.WHITE)
        print("Sensación térmica:                               ", Fore.GREEN + self.wind_chill         + Fore.WHITE)
        print("Índice de calor:                                 ", Fore.GREEN + self.heat_index         + Fore.WHITE)
        print("Índice THW:                                      ", Fore.GREEN + self.thw_index          + Fore.WHITE)
        print("Índice THSW:                                     ", Fore.GREEN + self.thsw_index         + Fore.WHITE)
        print("Lluvia acumulada:                                ", Fore.GREEN + self.rain               + Fore.WHITE)
        print("Tasa de lluvia:                                  ", Fore.GREEN + self.rain_rate          + Fore.WHITE)
        print("Radiación solar:                                 ", Fore.GREEN + self.solar_rad          + Fore.WHITE)
        print("Energía solar:                                   ", Fore.GREEN + self.solar_energy       + Fore.WHITE)
        print("Radiación solar máxima:                          ", Fore.GREEN + self.hi_solar_rad       + Fore.WHITE)
        print("Índice de calor solar:                           ", Fore.GREEN + self.solar_heat_index   + Fore.WHITE)
        print("Índice UV:                                       ", Fore.GREEN + self.uv_index           + Fore.WHITE)
        print("Dosis UV:                                        ", Fore.GREEN + self.uv_dose            + Fore.WHITE)
        print("Temperatura interior:                            ", Fore.GREEN + self.in_temp            + Fore.WHITE)
        print("Humedad interior:                                ", Fore.GREEN + self.in_hum             + Fore.WHITE)
        print("Punto de rocío interior:                         ", Fore.GREEN + self.in_dew             + Fore.WHITE)
        print("Índice de calor interior:                        ", Fore.GREEN + self.in_heat            + Fore.WHITE)
        print("Contenido de humedad absoluta interior:          ", Fore.GREEN + self.in_emc             + Fore.WHITE)
        print("Densidad interior:                               ", Fore.GREEN + self.in_density         + Fore.WHITE)
        print("Evapotranspiración:                              ", Fore.GREEN + self.et                 + Fore.WHITE)
        print("Muestras de velocidad del viento:                ", Fore.GREEN + self.wind_samp          + Fore.WHITE)
        print("Transmisiones de velocidad del viento:           ", Fore.GREEN + self.wind_tx            + Fore.WHITE)
        print("Recepciones ISS:                                 ", Fore.GREEN + self.iss_recept         + Fore.WHITE)
        print("Interrupciones de arco:                          ", Fore.GREEN + self.arc_int            + Fore.WHITE) 

        

while True:
    try:
        response = requests.get(url)
        response.raise_for_status()
        break # Rompe el bucle si la solicitud es exitosa
    except requests.exceptions.RequestException:
        os.system("cls")
        trys +=1
        print("Error al realizar la solicitud. Reintentando(",trys,")...")


lastjump = response.text.rfind("\n")
text = response.text[0:lastjump]
prelastjum = text.rfind("\n")
text = response.text[prelastjum+1:lastjump]

values = text.split()

weatherreport = WeatherData(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11], values[12], values[13], values[14], values[15], values[16], values[17], values[18], values[19], values[20], values[21], values[22], values[23], values[24], values[25], values[26], values[27], values[28], values[29], values[30], values[31], values[32], values[33], values[34])




timevalues = values[0].split("/")
timevalues2 = values[1].split(":")
timevalues.append(timevalues2[0])
timevalues.append(timevalues2[1])

for i in range(len(timevalues)):
    timevalues[i] = int(timevalues[i])

datetime = datetime((timevalues[2]+2000), timevalues[1], timevalues[0], timevalues[3], timevalues[4])
now = datetime.now()
diff = now - datetime

# Obtener el número total de segundos
total_seconds = diff.total_seconds()

# Calcular los días, horas, minutos y segundos
days, remainder = divmod(total_seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

# Formatear el tiempo en una cadena de texto
if(days == 0):
    time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
else:
    time_str = f"{int(days)} días, {int(hours):02}:{int(minutes):02}:{int(seconds):02}"

print("Medicion tomada hace:", Fore.RED,time_str, Fore.WHITE, end="\n\n")
print("Datos obtenidos\n\n",Fore.CYAN + text + Fore.WHITE, end="\n\n")
print("Tabla de datos\n")
weatherreport.print_data()





