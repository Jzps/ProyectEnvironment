from auto import Auto

class AutoNuevo(Auto):
    def dar_mantenimiento(self):
        return f"El auto nuevo {self.marca} {self.modelo} está en perfectas condiciones, solo revisión básica."

class AutoUsado(Auto):
    def dar_mantenimiento(self):
        return f"El auto usado {self.marca} {self.modelo} recibió cambio de aceite y revisión completa."

class AutoElectrico(Auto):
    def dar_mantenimiento(self):
        return f"El auto eléctrico {self.marca} {self.modelo} recibió revisión de batería y sistema eléctrico."