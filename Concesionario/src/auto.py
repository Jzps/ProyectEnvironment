class Auto:
    def _init_(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"{self.marca} {self.modelo} - Precio: ${self.precio}"

    def dar_mantenimiento(self):
        return f"El auto {self.marca} {self.modelo} ha recibido mantenimiento general."