from database.config import SessionLocal
from crud import mantenimiento_crud
from schemas import MantenimientoCreate
from uuid import UUID


class MantenimientoService:
    def __init__(self, db=None):
        self.db = db or SessionLocal()

    def registrar_mantenimiento(
        self, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
    ):
        return mantenimiento_crud.registrar_mantenimiento(
            self.db, mantenimiento, usuario_id
        )

    def listar_mantenimientos(self):
        return mantenimiento_crud.obtener_mantenimientos(self.db)
