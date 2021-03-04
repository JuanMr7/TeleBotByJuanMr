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
class Aeropuerto:
    def __init__(self, datos_json):
        self.nombre = datos_json["nombre"]
        self.codCiudad = datos_json["ciud"]
        self.pais = datos_json["pais"]
        self.provincia = datos_json["provincia"]
        self.ciudad = datos_json["ciudad"]
        self.vuelos = []

    def generar_vuelos(self, aeropuertos, min_vuelos = 4, max_vuelos = 8):
        for i in range( 0, rd.randrange(min_vuelos, max_vuelos)):
            aeropuerto = self

            while aeropuerto == self:
                aeropuerto = aeropuertos[rd.randrange(0, len(aeropuertos))]

            hora = datetime.time(rd.randrange(0, 24), rd.randrange(0, 60))
            fecha = datetime.date.today() + datetime.timedelta(days= rd.randrange(1, 16))
            vuelo = Vuelo(aeropuerto, hora, fecha, self)
            self.vuelos.append(vuelo)

    def eliminar_vuelos(self):
        for vuelo in self.vuelos:
            print("Aeropuerto: " + vuelo.aeropuerto_destino)

    def __repr__(self):
        return "Aeropuerto: " + self.nombre + ", país: " + self.pais
