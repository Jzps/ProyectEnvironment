from auto import Auto

class AutoNuevo(Auto):
    def dar_mantenimiento(self):
        print("\n--- Selección de mantenimiento para auto NUEVO ---")
        print("1. Revisión básica de fábrica")
        print("2. Actualización de software del vehículo")
        print("3. Cambio de filtro de aire")

        opcion = input("Seleccione una opción de mantenimiento: ")

        if opcion == "1":
            return f"El auto nuevo {self.marca} {self.modelo} recibió revisión básica de fábrica."
        elif opcion == "2":
            return f"El auto nuevo {self.marca} {self.modelo} recibió actualización de software."
        elif opcion == "3":
            return f"El auto nuevo {self.marca} {self.modelo} recibió cambio de filtro de aire."
        else:
            return "Opción no válida."


class AutoUsado(Auto):
    def __init__(self, marca, modelo, precio, kilometraje):
        super().__init__(marca, modelo, precio)
        self.kilometraje = kilometraje

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}, Kilometraje: {self.kilometraje} km"
    
    def dar_mantenimiento(self):
        print("\n--- Selección de mantenimiento para auto USADO ---")
        print("1. Cambio de aceite y filtros")
        print("2. Revisión completa de motor")
        print("3. Revisión del sistema de frenos y suspensión")

        opcion = input("Seleccione una opción de mantenimiento: ")

        if opcion == "1":
            return f"El auto usado {self.marca} {self.modelo} recibió cambio de aceite y filtros."
        elif opcion == "2":
            return f"El auto usado {self.marca} {self.modelo} recibió revisión completa de motor."
        elif opcion == "3":
            return f"El auto usado {self.marca} {self.modelo} recibió revisión de frenos y suspensión."
        else:
            return "Opción no válida."


class AutoElectrico(Auto):
    def __init__(self, marca, modelo, precio, autonomia):
        super().__init__(marca, modelo, precio)
        self.autonomia = autonomia

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}, Autonomía: {self.autonomia} km"

    def dar_mantenimiento(self):
        print("\n--- Selección de mantenimiento para auto ELÉCTRICO ---")
        print("1. Revisión de batería")
        print("2. Revisión de sistema de carga")
        print("3. Optimización de autonomía")

        opcion = input("Seleccione una opción de mantenimiento: ")

        if opcion == "1":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió revisión de batería."
        elif opcion == "2":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió revisión de sistema de carga."
        elif opcion == "3":
            return f"El auto eléctrico {self.marca} {self.modelo} recibió optimización de autonomía."
        else:
            return "Opción no válida."
