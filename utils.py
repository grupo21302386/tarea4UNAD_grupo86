
from datetime import datetime

class DatoInvalidoError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass

class ReservaInvalidaError(Exception):
    pass

def registrar_log(mensaje):
    with open("errores.log", "a", encoding="utf-8") as archivo:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")