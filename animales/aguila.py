from ser_vivo import SerVivo


class Aguila(SerVivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "montana", "peces y ratones", tamano, color)

    def desplazarse(self):
        return f"{self.nombre} vuela alto sobre la montana"

    def instintos(self):
        return f"{self.nombre} caza con su vista muy fina"
