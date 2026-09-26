from botella import botella
from botella_plastico import botella_plastico
from botella_vidrio import botella_vidrio


def pedir_entero(mensaje, minimo=0, maximo=None):
    while True:
        try:
            valor = int(input(mensaje).strip())
        except ValueError:
            print("Introduce un número entero.")
            continue
        if valor < minimo:
            print(f"El valor no puede ser menor que {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"El valor no puede ser mayor que {maximo}.")
            continue
        return valor


def pedir_texto(mensaje, defecto):
    respuesta = input(mensaje).strip()
    return respuesta or defecto


class principal:
    TIPOS = {
        "plastico": botella_plastico,
        "vidrio": botella_vidrio,
        "generica": botella,
    }

    def __init__(self):
        self.botellas = []

    def crear(self, tipo):
        clase = self.TIPOS[tipo]
        capacidad = pedir_entero("Capacidad en ml: ", minimo=1)
        contenido = pedir_entero("Contenido inicial en ml: ", minimo=0, maximo=capacidad)
        forma = pedir_texto(f"Forma [{clase.FORMA}]: ", clase.FORMA)
        diseno = pedir_texto(f"Diseño [{clase.DISENO}]: ", clase.DISENO)
        tapa = pedir_texto(f"Tapa [{clase.TAPA}]: ", clase.TAPA)

        nueva = clase(capacidad, contenido, forma, diseno, tapa)
        self.botellas.append(nueva)
        print(f"\nBotella creada: {nueva}")

    def mostrar(self):
        if not self.botellas:
            print("Todavía no has creado ninguna botella.")
            return
        print("\n--- Botellas creadas ---")
        for posicion, botella_actual in enumerate(self.botellas, start=1):
            print(f"{posicion}. {botella_actual}")

    def elegir_botella(self):
        if not self.botellas:
            print("Todavía no has creado ninguna botella.")
            return None
        self.mostrar()
        posicion = pedir_entero("Número de botella: ", minimo=1, maximo=len(self.botellas))
        return self.botellas[posicion - 1]

    def ficha(self):
        elegida = self.elegir_botella()
        if elegida is None:
            return
        print("\n===== FICHA TÉCNICA =====")
        print(elegida.ficha())
        print("=======================")

    def llenar(self):
        elegida = self.elegir_botella()
        if elegida is None:
            return
        cantidad = pedir_entero("Cantidad en ml (0 = llenar del todo): ", minimo=0)
        elegida.llenar(cantidad if cantidad else None)
        print(f"Quedó así: {elegida}")

    def vaciar(self):
        elegida = self.elegir_botella()
        if elegida is None:
            return
        elegida.vaciar()
        print(f"Botella vacía: {elegida}")

    def menu(self):
        while True:
            print("\n=== PROYECTO BOTELLA ===")
            print("1) Crear botella de plástico")
            print("2) Crear botella de vidrio")
            print("3) Crear botella genérica")
            print("4) Ver botellas creadas")
            print("5) Ver ficha técnica")
            print("6) Llenar una botella")
            print("7) Vaciar una botella")
            print("0) Salir")

            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                self.crear("plastico")
            elif opcion == "2":
                self.crear("vidrio")
            elif opcion == "3":
                self.crear("generica")
            elif opcion == "4":
                self.mostrar()
            elif opcion == "5":
                self.ficha()
            elif opcion == "6":
                self.llenar()
            elif opcion == "7":
                self.vaciar()
            elif opcion == "0":
                print("Hasta luego.")
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    principal().menu()
