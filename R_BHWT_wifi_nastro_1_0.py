# Taller Programación y Robótica en CMM BML – 2024 -2025 - Clase wifi
# Programa: Test de conexion a wifi y hacer un get numero astronautas en espacio
# Hardware platform: Pico W solamente
# Librerias : sh1106.py
# Ref librerias: https://github.com/robert-hh/SH1106
# Fecha JCSP 2023 02 06
# Licencia : CC BY-NC-SA 4.0

from os import uname
# Informative block - start
p_keyOhw = "I2C en GPIO 4&5 = SDA0 & SCL0 400khz"
p_project = "Test de conexion a wifi y hacer un get numero astronautas en espacio"
p_version = "1.0"
p_library = "SH1106  @robert-hh + requests"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")

from machine import Pin, I2C
import sh1106
from do_connect import *
import requests

# 0.0 - Constates y varaibles globales
WIDTH =128 
HEIGHT= 64
FREQ = 400_000   # Try lowering this value in case of "Errno 5"

# 1- Creacion del objeto display, antes i2c
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = FREQ)
display = sh1106.SH1106_I2C(WIDTH,
                            HEIGHT,
                            i2c,
                            res = None,
                            addr = 0x3c,
                            rotate = 0) # valores 0, 90, 180, 270
display.sleep(False)
display.fill(0)
display.text('Test Wifi', 0, 0, 1)
display.show()
# 2- Nos conectamos a Internet
ip = do_connect()
display.text(ip, 0, 10, 1)
display.show()
url = "http://api.open-notify.org/astros.json" # Cuantos humanos hay en el eespacio ahora?
endPoint = url
respuesta = requests.get(endPoint)
display.text('Num astro/nombre', 0, 20, 1)
display.text(str(respuesta.json()['number']), 0, 30, 1)
display.text(respuesta.json()['people'][0]['name'], 0, 40, 1)
display.show()