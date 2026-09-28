from ser_vivo import SerVivo
from lobo import Lobo
from tortuga import Tortuga
from aguila import Aguila
from mariposa import Mariposa
from rana import Rana

lobo_gris = Lobo("Lobo gris", 4, "grande", "gris")
tortuga_marina = Tortuga("Tortuga marina", 20, "mediana", "verde oscuro")
aguila_real = Aguila("Aguila real", 7, "grande", "marron claro")
mariposa_morada = Mariposa("Mariposa", 1, "pequena", "morada")
rana_verde = Rana("Rana", 2, "pequena", "verde")

print(lobo_gris.desplazarse())
print(lobo_gris.comunicarse())
print(lobo_gris.reproducirse())
print(lobo_gris.comer())
print(lobo_gris.adaptacion())
print(lobo_gris.instintos())
print(lobo_gris.descansar())
print(lobo_gris.dormir())
print(lobo_gris.convivir())

print(tortuga_marina.desplazarse())
print(tortuga_marina.adaptacion())

print(aguila_real.desplazarse())
print(aguila_real.instintos())

print(mariposa_morada.desplazarse())
print(mariposa_morada.adaptacion())

print(rana_verde.desplazarse())
print(rana_verde.adaptacion())
