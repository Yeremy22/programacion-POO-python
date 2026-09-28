class SerVivo:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def desplazarse(self):
        return f"{self.nombre} se desplaza por su {self.habitat}"

    def comunicarse(self):
        return f"{self.nombre} se comunica con sonidos y movimientos"

    def reproducirse(self):
        return f"{self.nombre} tiene crias"

    def comer(self):
        return f"{self.nombre} se alimenta de {self.dieta}"

    def adaptacion(self):
        return f"{self.nombre} esta adaptado a su {self.habitat}"

    def instintos(self):
        return f"{self.nombre} sigue sus instintos para buscar {self.dieta}"

    def descansar(self):
        return f"{self.nombre} descansa en su {self.habitat}"

    def dormir(self):
        return f"{self.nombre} duerme por la noche"

    def convivir(self):
        return f"{self.nombre} vive en grupo con otros de su {self.habitat}"
