from ser_vivo import SerVivo


class Tortuga(SerVivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "rio y playa", "plantas y algas", tamano, color)

    def desplazarse(self):
        return f"{self.nombre} camina lento y nada si hace falta"

    def adaptacion(self):
        return f"{self.nombre} se adapta al agua con su caparazon"
