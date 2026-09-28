from ser_vivo import SerVivo


class Rana(SerVivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "charca", "moscas e insectos", tamano, color)

    def desplazarse(self):
        return f"{self.nombre} salta y nada en la charca"

    def adaptacion(self):
        return f"{self.nombre} se adapta al agua y a la tierra"
