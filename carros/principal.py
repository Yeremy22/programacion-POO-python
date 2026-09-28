from carro import Carro
from carro_deportivo import CarroDeportivo
from carro_furgoneta import CarroFurgoneta
from carro_camion import CarroCamion

obj_deportivo = CarroDeportivo("Convertible", "negro", "3.0", 2, 2)
obj_furgoneta = CarroFurgoneta("Van reparto", "blanca", "2.5", 4, 3)
obj_camion = CarroCamion("Volqueta", "blanco", "6.0", 2, 3)

print(obj_deportivo.arrancar())
print(obj_deportivo.acelerar_y_frenar("acelerar", 100))
print(obj_deportivo.acelerar_y_frenar("frenar", 40))
print(obj_deportivo.apagar())
print(obj_deportivo.sistema_direccion("asistida"))
print(obj_deportivo.climatizacion("encendida"))
print(obj_deportivo.tipo_seguridad())
print(obj_deportivo.luces("encendidas"))
print(obj_deportivo.sistema_ventanas("abiertas"))
print(obj_deportivo.sistema_espejo("ajustados"))

print(obj_furgoneta.arrancar())
print(obj_furgoneta.sistema_ventanas("cerradas"))
print(obj_furgoneta.tipo_seguridad())

print(obj_camion.arrancar())
print(obj_camion.sistema_ventanas("cerradas"))
print(obj_camion.sistema_espejo("plegados"))
