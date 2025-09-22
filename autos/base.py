class Auto:
    """
    Representa un automóvil genérico.

    Attributes:
        marca (str): Marca del auto.
        modelo (str): Modelo del auto.
        precio (float): Precio en la moneda local.
    """

    def __init__(self, marca, modelo, precio):
        """
        Inicializa un nuevo objeto Auto.

        :param marca: Marca del auto.
        :param modelo: Modelo del auto.
        :param precio: Precio en la moneda local.
        """
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        """
        Devuelve la información básica del auto formateada.

        :return: Texto con marca, modelo y precio.
        :rtype: str
        """
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"
