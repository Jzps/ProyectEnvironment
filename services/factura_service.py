from database.config import SessionLocal
from crud import mantenimiento_crud, factura_crud, auto_crud
from schemas.factura_schema import FacturaCreate
from uuid import UUID


class FacturaService:
    def __init__(self, db=None):
        self.db = db or SessionLocal()

    def crear_factura(self, factura: FacturaCreate, usuario_id: UUID | None = None):
        auto = auto_crud.obtener_auto_por_id(self.db, factura.auto_id)
        if not auto or not auto.vendido:
            print("El auto no existe o no está vendido.")
            return None

        mantenimientos = mantenimiento_crud.obtener_mantenimientos_por_auto(
            self.db, factura.auto_id
        )
        costo_mantenimiento_total = sum(m.costo for m in mantenimientos)

        factura.total = (
            factura.precio_carro_base + costo_mantenimiento_total - factura.descuento
        )
        factura.costo_mantenimiento = costo_mantenimiento_total

        return factura_crud.crear_factura(self.db, factura, usuario_id)

    def listar_facturas(self):
        return factura_crud.obtener_facturas(self.db)

    def eliminar_factura(self, factura_id: UUID):
        return factura_crud.eliminar_factura(self.db, factura_id)
