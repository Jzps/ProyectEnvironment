from database.config import SessionLocal
from crud import factura_crud
from schemas import FacturaCreate

class FacturaService:
    def __init__(self):
        self.db = SessionLocal()

    def crear_factura(self, factura: FacturaCreate):
        return factura_crud.crear_factura(self.db, factura)

    def listar_facturas(self):
        return factura_crud.obtener_facturas(self.db)
