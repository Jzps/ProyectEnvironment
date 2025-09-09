from database.config import SessionLocal
from crud import auto_crud
from schemas.auto_schema import AutoCreate
from autos import AutoNuevo, AutoUsado, AutoElectrico

class Concesionario:
    def __init__(self):
        self.db = SessionLocal()

    def comprar_auto(self, auto):
        auto_schema = AutoCreate(
            marca=auto.marca,
            modelo=auto.modelo,
            precio=auto.precio,
            tipo=auto.__class__.__name__,
            extra=str(getattr(auto, "kilometraje", getattr(auto, "autonomia", None)))
        )
        auto_crud.crear_auto(self.db, auto_schema)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    def mostrar_autos(self):
        autos = auto_crud.obtener_autos(self.db)
        if not autos:
            print("No hay autos en el concesionario.")
        else:
            for i, auto in enumerate(autos, start=1):
                print(f"{i}. {auto.marca} {auto.modelo} ({auto.tipo}) - ${auto.precio}")

    def vender_auto(self, indice: int):
        autos = auto_crud.obtener_autos(self.db)
        if 0 <= indice - 1 < len(autos):
            auto = autos[indice - 1]
            eliminado = auto_crud.eliminar_auto(self.db, auto.id)
            print(f"Se ha vendido: {eliminado.marca} {eliminado.modelo}")
        else:
            print("Índice inválido, no se pudo vender el auto.")

    def dar_mantenimiento(self, indice: int):
        autos = auto_crud.obtener_autos(self.db)
        if 0 <= indice - 1 < len(autos):
            auto_db = autos[indice - 1]

            if auto_db.tipo == "AutoNuevo":
                auto_obj = AutoNuevo(auto_db.marca, auto_db.modelo, auto_db.precio)
            elif auto_db.tipo == "AutoUsado":
                auto_obj = AutoUsado(auto_db.marca, auto_db.modelo, auto_db.precio, int(auto_db.extra))
            elif auto_db.tipo == "AutoElectrico":
                auto_obj = AutoElectrico(auto_db.marca, auto_db.modelo, auto_db.precio, int(auto_db.extra))
            else:
                print("Tipo de auto no reconocido.")
                return

            resultado = auto_obj.dar_mantenimiento()
            print(resultado)
        else:
            print("Índice inválido, no se pudo dar mantenimiento.")
