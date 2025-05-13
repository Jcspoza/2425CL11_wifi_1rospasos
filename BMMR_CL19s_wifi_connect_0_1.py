# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 20
# Goal : Conexion SUPER basica de redes wifi
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/1.access.html

# Informative block - start
p_ucontroler = "Pico W SOLO"
p_keyOhw = "Nada"
p_project = "Connection wifi networks - super basic"
p_version = "0.1"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import network # varias funciones y objetos requeridos para la conexion wifi
from secrets import * # guardados en secrets conmo diccionario SSID y PASSWORD

wlan = network.WLAN(network.STA_IF) # Crea un objeto wireless local area network en modo estacion
wlan.active(True) # activa el circuito wifi - tarda unos segundos
wlan.connect(secrets['ssid'], secrets['password']) # se conecta a al red wifi SSID con al PASSWORD,

print(wlan.isconnected()) # Check de si esta conectado