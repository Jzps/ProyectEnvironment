class Concesionario:
    def __init__(self):
        self.autos = []

    def comprar_auto(self, auto):
        self.autos.append(auto)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    def vender_auto(self, indice):
        if 0 <= indice < len(self.autos):
            auto_vendido = self.autos.pop(indice)
            print(f"Se ha vendido: {auto_vendido.mostrar_info()}")
        else:
            print("Índice inválido, no se pudo vender el auto.")

    def mostrar_autos(self):
        if not self.autos:
            print("No hay autos en el concesionario.")
        else:
            for i, auto in enumerate(self.autos, start = 1):
                print(f"{i}. {auto.mostrar_info()}")

    def dar_mantenimiento(self, indice):
        if 0 <= indice < len(self.autos):
            auto = self.autos[indice]
            print(auto.dar_mantenimiento())
        else:
            print("Índice inválido, no se pudo dar mantenimiento.")
