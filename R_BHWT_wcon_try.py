from do_connect import *

try:
    ip = do_connect()
    print(ip)
except RuntimeError as e:
    print(f"Error en conexion wifi: {e}")