from database.config import SessionLocal
from crud import mantenimiento_crud
from schemas import MantenimientoCreate

class MantenimientoService:
    def __init__(self, db=None):
        if db is None:
            self.db = SessionLocal()
        else:
            self.db = db

    def registrar_mantenimiento(self, mantenimiento: MantenimientoCreate):
        return mantenimiento_crud.registrar_mantenimiento(self.db, mantenimiento)

    def listar_mantenimientos(self):
        return mantenimiento_crud.obtener_mantenimientos(self.db)
