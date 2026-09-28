from carro import Carro


class CarroFurgoneta(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diesel")

    def sistema_ventanas(self, estado):
        return f"Ventanas {estado} y puerta trasera con carga"

    def tipo_seguridad(self):
        return "Airbags, sensores de retroceso y cinturon de seguridad"
