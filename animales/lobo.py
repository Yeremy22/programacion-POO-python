from ser_vivo import SerVivo


class Lobo(SerVivo):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "bosque frio", "carne", tamano, color)

    def desplazarse(self):
        return f"{self.nombre} corre junto a su manada"

    def comunicarse(self):
        return f"{self.nombre} aulla para llamar a su manada"
