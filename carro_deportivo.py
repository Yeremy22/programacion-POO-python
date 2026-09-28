from carro import Carro


class CarroDeportivo(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def sistema_direccion(self, tipo):
        return f"El deportivo usa direccion {tipo} y es muy deportivo"

    def tipo_seguridad(self):
        return "Airbags, ABS y cinturon de seguridad"
