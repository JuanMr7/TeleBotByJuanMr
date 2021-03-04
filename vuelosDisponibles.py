import datetime
import random as rd

class Vuelo:
    def __init__(self, aeropuerto_destino, hora, fecha, aeropuerto_origen):
        self.aeropuerto_origen = aeropuerto_origen
        self.aeropuerto_destino = aeropuerto_destino
        self.hora = hora
        self.fecha = fecha
        self.asientos = 150

    def __repr__(self):
        return "Aeropuerto destino: " + self.aeropuerto_destino.__repr__() + ", fecha: " + self.fecha.isoformat() +", hora: " + self.hora.isoformat()
