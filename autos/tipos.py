from autos.base import Auto

class AutoNuevo(Auto):
    """
    Representa un auto nuevo.

    Hereda de:
        Auto

    Métodos:
        dar_mantenimiento():
            Muestra un menú de mantenimiento específico para autos nuevos
            y retorna el resultado de la acción elegida.
    """

    def dar_mantenimiento(self):
        print(f"\n--- Mantenimiento para Auto Nuevo {self.marca} {self.modelo} ---")
        print("1. Revisión básica")
        print("2. Lavado")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return f"El auto nuevo {self.marca} {self.modelo} recibió revisión básica."
        elif opcion == "2":
            return f"El auto nuevo {self.marca} {self.modelo} fue lavado."
        else:
            return "Opción inválida."
    """
    Muestra las opciones de mantenimiento para un auto nuevo y
        retorna un mensaje indicando la acción realizada.

    Returns:
        str: Descripción del mantenimiento realizado o mensaje de error
             si la opción no es válida.
    """
        
class AutoUsado(Auto): 
    """
    Representa un auto usado, que incluye información de kilometraje.

    Hereda de:
        Auto

    Atributos adicionales:
        kilometraje (int): Kilómetros recorridos por el auto.

    Métodos:
        mostrar_info():
            Retorna la información del auto incluyendo su kilometraje.
        dar_mantenimiento():
            Muestra un menú de mantenimiento para autos usados
            y retorna el resultado de la acción elegida.
    """

    def __init__(self, marca, modelo, precio, kilometraje):
        super().__init__(marca, modelo, precio)
        self.kilometraje = kilometraje
    """
    Inicializa un auto usado.

        Args:
            marca (str): Marca del auto.
            modelo (str): Modelo del auto.
            precio (float): Precio del auto.
            kilometraje (int): Kilómetros recorridos.
    """

    def mostrar_info(self):
        return super().mostrar_info() + f", Kilometraje: {self.kilometraje} km"
    """
     Retorna la información completa del auto usado.

    Returns:
        str: Información base del auto con su kilometraje.
    """

    def dar_mantenimiento(self):
        """
        Muestra las opciones de mantenimiento para un auto usado y
        retorna un mensaje indicando la acción realizada.

        Returns:
            str: Descripción del mantenimiento realizado o mensaje de error
                 si la opción no es válida.
        """

        print(f"\n--- Mantenimiento para Auto Usado {self.marca} {self.modelo} ---")
        print("1. Cambio de aceite")
        print("2. Revisión general")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            return f"El auto usado {self.marca} {self.modelo} recibió cambio de aceite."
        elif opcion == "2":
            return f"El auto usado {self.marca} {self.modelo} recibió revisión general."
        else:
            return "Opción inválida."


class AutoElectrico(Auto):
    """
    Representa un auto eléctrico, que incluye información de autonomía.

    Hereda de:
        Auto

    Atributos adicionales:
        autonomia (int): Autonomía de la batería en kilómetros.

    Métodos:
        mostrar_info():
            Retorna la información del auto incluyendo su autonomía.
        dar_mantenimiento():
            Muestra un menú de mantenimiento para autos eléctricos
            y retorna el resultado de la acción elegida.
    """

    def __init__(self, marca, modelo, precio, autonomia):
        super().__init__(marca, modelo, precio)
        self.autonomia = autonomia
        """
        Inicializa un auto eléctrico.

        Args:
            marca (str): Marca del auto.
            modelo (str): Modelo del auto.
            precio (float): Precio del auto.
            autonomia (int): Autonomía de la batería en km.
        """

    def mostrar_info(self):
        return super().mostrar_info() + f", Autonomía: {self.autonomia} km"
    """
        Retorna la información completa del auto eléctrico.

        Returns:
            str: Información base del auto con su autonomía.
        """

    def dar_mantenimiento(self):
        """
        Muestra las opciones de mantenimiento para un auto eléctrico y
        retorna un mensaje indicando la acción realizada.

        Returns:
            str: Descripción del mantenimiento realizado o mensaje de error
                 si la opción no es válida.
        """

        print(f"\n--- Mantenimiento para Auto Eléctrico {self.marca} {self.modelo} ---")
        print("1. Revisión de batería")
        print("2. Actualización de software")
        opcion = input("Seleccione una opción: ")
        

        if opcion == "1":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió revisión de batería."
        elif opcion == "2":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió actualización de software."
        else:
            return "Opción inválida."
