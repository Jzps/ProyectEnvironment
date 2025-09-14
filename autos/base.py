class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"
