class botella:
    """Clase base: material, capacidad, forma, diseño y tapa + comportamiento."""

    MATERIAL = "genérico"
    FORMA = "cilíndrica"
    DISENO = "liso"
    TAPA = "sin tapa"

    def __init__(self, capacidad, contenido=0, forma=FORMA, diseno=DISENO, tapa=TAPA,
                 material=MATERIAL):
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que 0.")
        if contenido < 0:
            raise ValueError("El contenido no puede ser negativo.")
        if contenido > capacidad:
            raise ValueError("El contenido no puede superar la capacidad.")
        if not forma or not diseno or not tapa:
            raise ValueError("La forma, el diseño y la tapa son obligatorios.")

        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.contenido = contenido

    @property
    def espacio_disponible(self):
        return self.capacidad - self.contenido

    @property
    def esta_llena(self):
        return self.contenido == self.capacidad

    @property
    def esta_vacia(self):
        return self.contenido == 0

    def liquidos(self):
        return "agua y bebidas de consumo habitual"

    def facilitar_vertido(self):
        return "el cuello estrecho permite un vertido controlado"

    def cierre_hermetico(self):
        return False

    def transporte(self):
        return "cómoda de llevar en mochila o en el bolso"

    def manejo(self):
        return "fácil de manejar con una sola mano"

    def compatibilidad_bebidas_calientes(self):
        return False

    def compatibilidad_bebidas_frias(self):
        return True

    def reutilizacion(self):
        return "reutilizable mientras no se rompa o se agriete"

    def transparencia(self):
        return "depende del acabado: puede ser transparente u opaca"

    def llenar(self, cantidad=None):
        """Llena la botella. Sin cantidad, la llena hasta el tope."""
        if cantidad is None:
            self.contenido = self.capacidad
        else:
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa.")
            self.contenido = min(self.contenido + cantidad, self.capacidad)
        return self.contenido

    def vaciar(self):
        self.contenido = 0
        return self.contenido

    def ficha(self):
        return (f"MATERIAL: {self.material}\n"
                f"Capacidad: {self.capacidad} ml\n"
                f"Forma: {self.forma}\n"
                f"Diseño: {self.diseno}\n"
                f"Tapa: {self.tapa}\n"
                f"Contenido: {self.contenido} ml (libre: {self.espacio_disponible} ml)\n"
                f"- Líquidos: {self.liquidos()}\n"
                f"- Facilitar el vertido: {self.facilitar_vertido()}\n"
                f"- Cierre hermético: {'sí' if self.cierre_hermetico() else 'no'}\n"
                f"- Transporte: {self.transporte()}\n"
                f"- Manejo: {self.manejo()}\n"
                f"- Bebidas calientes: "
                f"{'sí' if self.compatibilidad_bebidas_calientes() else 'no'}\n"
                f"- Bebidas frías: "
                f"{'sí' if self.compatibilidad_bebidas_frias() else 'no'}\n"
                f"- Reutilización: {self.reutilizacion()}\n"
                f"- Transparencia: {self.transparencia()}")

    def __str__(self):
        return (f"{type(self).__name__} de {self.material} | {self.capacidad} ml | "
                f"forma: {self.forma} | diseño: {self.diseno} | tapa: {self.tapa} | "
                f"contenido: {self.contenido} ml | libre: {self.espacio_disponible} ml")
