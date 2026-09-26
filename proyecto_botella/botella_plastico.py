from botella import botella


class botella_plastico(botella):
    """Botella de plástico (PET): ligera, resistente a golpes y barata."""

    MATERIAL = "plástico"
    FORMA = "cilíndrica con nervios"
    DISENO = "liso y transparente"
    TAPA = "rosca de plástico"

    def __init__(self, capacidad, contenido=0, forma=FORMA, diseno=DISENO, tapa=TAPA):
        super().__init__(capacidad, contenido, forma, diseno, tapa, material=self.MATERIAL)

    def liquidos(self):
        return "agua, zumo, refrescos y bebidas frías; no para líquidos muy calientes"

    def facilitar_vertido(self):
        return "cuello fino y rosca: se vierte sin derramar"

    def cierre_hermetico(self):
        return True

    def transporte(self):
        return "muy ligera y resistente a caidas: ideal para deporte o excursiones"

    def manejo(self):
        return "los nervios del diseño evitan que se resbale"

    def compatibilidad_bebidas_calientes(self):
        return False

    def compatibilidad_bebidas_frias(self):
        return True

    def reutilizacion(self):
        return "unas 100 veces si se lava a mano"

    def transparencia(self):
        return "transparente si es PET claro, opaca si lleva color"
