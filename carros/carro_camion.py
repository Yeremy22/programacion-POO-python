from carro import Carro


class CarroCamion(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diesel")

    def sistema_ventanas(self, estado):
        return f"Ventanas {estado} y solo tiene ventanas en la cabina"

    def sistema_espejo(self, estado):
        return f"Espejos {estado} grandes para ver los puntos ciegos"
