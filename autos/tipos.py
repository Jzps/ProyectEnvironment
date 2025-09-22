from autos.base import Auto


class AutoNuevo(Auto):
    """
    Representa un auto nuevo.

    Hereda de Auto.
    """

    def dar_mantenimiento(self):
        """
        Muestra un menú de mantenimiento para autos nuevos y retorna la acción realizada.
        :return: Descripción del mantenimiento realizado o mensaje de error.
        :rtype: str
        """
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


class AutoUsado(Auto):
    """
    Representa un auto usado, con información de kilometraje.

    Hereda de Auto.
    Atributos adicionales:
        kilometraje (int): Kilómetros recorridos por el auto.
    """

    def __init__(self, marca, modelo, precio, kilometraje):
        super().__init__(marca, modelo, precio)
        self.kilometraje = kilometraje

    def mostrar_info(self):
        """
        Retorna la información del auto usado incluyendo su kilometraje.
        :return: Información completa del auto.
        :rtype: str
        """
        return super().mostrar_info() + f", Kilometraje: {self.kilometraje} km"

    def dar_mantenimiento(self):
        """
        Muestra un menú de mantenimiento para autos usados y retorna la acción realizada.
        :return: Descripción del mantenimiento realizado o mensaje de error.
        :rtype: str
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
    Representa un auto eléctrico con información de autonomía.

    Hereda de Auto.
    Atributos adicionales:
        autonomia (int): Autonomía de la batería en kilómetros.
    """

    def __init__(self, marca, modelo, precio, autonomia):
        super().__init__(marca, modelo, precio)
        self.autonomia = autonomia

    def mostrar_info(self):
        """
        Retorna la información del auto eléctrico incluyendo su autonomía.
        :return: Información completa del auto.
        :rtype: str
        """
        return super().mostrar_info() + f", Autonomía: {self.autonomia} km"

    def dar_mantenimiento(self):
        """
        Muestra un menú de mantenimiento para autos eléctricos y retorna la acción realizada.
        :return: Descripción del mantenimiento realizado o mensaje de error.
        :rtype: str
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
