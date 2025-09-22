from database.config import SessionLocal
from crud import mantenimiento_crud
from schemas import MantenimientoCreate
from uuid import UUID


class MantenimientoService:
    """
    Servicio para gestionar los mantenimientos de autos.

    Permite registrar y consultar mantenimientos realizados.
    """

    def __init__(self, db=None):
        """Inicializa el servicio con una sesión de base de datos."""
        self.db = db or SessionLocal()

    def registrar_mantenimiento(
        self, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
    ):
        """
        Registra un mantenimiento en la base de datos para un auto específico.
        """
        return mantenimiento_crud.registrar_mantenimiento(
            self.db, mantenimiento, usuario_id
        )

    def listar_mantenimientos(self):
        """Devuelve todos los mantenimientos registrados."""
        return mantenimiento_crud.obtener_mantenimientos(self.db)
