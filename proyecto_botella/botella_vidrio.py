from botella import botella


class botella_vidrio(botella):
    """Botella de vidrio: hermética, reutilizable y apta para bebidas calientes."""

    MATERIAL = "vidrio"
    FORMA = "curva con cuello estrecho"
    DISENO = "estriado y transparente"
    TAPA = "tapa metálica de rosca"

    def __init__(self, capacidad, contenido=0, forma=FORMA, diseno=DISENO, tapa=TAPA):
        super().__init__(capacidad, contenido, forma, diseno, tapa, material=self.MATERIAL)

    def liquidos(self):
        return "agua, zumo, vino y bebidas frías o calientes"

    def facilitar_vertido(self):
        return "cuello de boca estrecha: control total al servir"

    def cierre_hermetico(self):
        return True

    def transporte(self):
        return "pesada y frágil: mejor en bolso con bolsillo o en caja"

    def manejo(self):
        return "hay que sujetarla bien: se resbala si está mojada o caliente"

    def compatibilidad_bebidas_calientes(self):
        return True

    def compatibilidad_bebidas_frias(self):
        return True

    def reutilizacion(self):
        return "casi indefinida: admite lavavillas y se puede desinfectar"

    def transparencia(self):
        return "muy transparente: se ve el nivel de contenido"
