class Auto:
    """
    Representa un automóvil genérico.

    Attributes:
        marca (str): Marca del auto.
        modelo (str): Modelo del auto.
        precio (float): Precio en la moneda local.
    """
    
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    """
        Inicializa un nuevo objeto Auto.

        Args:
            marca (str): Marca del auto.
            modelo (str): Modelo del auto.
            precio (float): Precio en la moneda local.
    """

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"
    """
        Devuelve un texto con la información básica del auto.

        Returns:
            str: Información formateada de marca, modelo y precio.
        """
