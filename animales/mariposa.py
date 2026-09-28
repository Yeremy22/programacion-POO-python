from ser_vivo import SerVivo


class Mariposa(SerVivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "jardin", "nectar de flores", tamano, color)

    def desplazarse(self):
        return f"{self.nombre} vuela de flor en flor"

    def adaptacion(self):
        return f"{self.nombre} se camufla con sus alas {self.color}"
