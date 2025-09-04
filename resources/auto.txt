class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"

    def dar_mantenimiento(self):
        print("\n--- Selección de mantenimiento general ---")
        print("1. Lavado general")
        print("2. Alineación y balanceo")
        print("3. Revisión de frenos")

        opcion = input("Seleccione una opción de mantenimiento: ")

        if opcion == "1":
            return f"El auto {self.marca} {self.modelo} recibió un lavado general."
        elif opcion == "2":
            return f"El auto {self.marca} {self.modelo} recibió alineación y balanceo."
        elif opcion == "3":
            return f"El auto {self.marca} {self.modelo} recibió revisión de frenos."
        else:
            return "Opción no válida."
