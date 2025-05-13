# Hardware platform: Pico W
# Author : JC Santamaria 
# Date : 2023 - 7 - 25
# Goal : Conexion basica de redes wifi
# Ref https://docs.sunfounder.com/projects/kepler-kit/en/latest/iotproject/1.access.html
# 0.1 -> 0.2 bucle de espera

# Informative block - start
p_ucontroler = "Pico W SOLO"
p_keyOhw = "Nada"
p_project = "Connection wifi networks - basic & time"
p_version = "0.2"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

import network # varias funciones y objetos requeridos para la conexion wifi
from secrets import * # guardados en secrets conmo diccionario SSID y PASSWORD
from utime import sleep, ticks_ms, ticks_diff

print('Connecting to WiFi Network Name:', secrets['ssid'])
wlan = network.WLAN(network.STA_IF) # Crea un objeto wireless local area network en modo estacion
wlan.active(True) # activa el circuito wifi - tarda unos segundos

start = ticks_ms() # Inicializamos una variable para contar el tiempo en milisegundos

if not wlan.isconnected(): # Check de si esta conectado
    wlan.connect(secrets['ssid'], secrets['password']) # se conecta a al red wifi SSID
    print("Waiting for connection...")
    counter = 0
    while not wlan.isconnected(): # Check de si esta conectado
        sleep(1)
        print(counter, '.', sep='', end='')
        counter += 1
        
delta = ticks_diff(ticks_ms(), start)
# no se debe hacer una resta, porque son contadores que "dan la vuelta"
print("Connect Time:", delta, 'milliseconds')
print('IP Address:', wlan.ifconfig()[0])
