from database.config import SessionLocal
from crud import mantenimiento_crud
from schemas import MantenimientoCreate
from uuid import UUID


class MantenimientoService:
    """
    Servicio para gestionar los mantenimientos de autos.

    Permite registrar mantenimientos, listar todos los mantenimientos
    registrados y asociarlos a autos y técnicos.
    """

    def __init__(self, db=None):
        """
        Inicializa el servicio de mantenimientos con una sesión de base de datos.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se proporciona, se crea una nueva.
        """

        self.db = db or SessionLocal()

    def registrar_mantenimiento(
        self, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
    ):
        """
        Registra un nuevo mantenimiento para un auto específico.

        Args:
            mantenimiento (MantenimientoCreate): Datos del mantenimiento a registrar.
            usuario_id (UUID | None): ID del usuario que realiza la acción.

        Returns:
            Mantenimiento registrado.
        """

        return mantenimiento_crud.registrar_mantenimiento(
            self.db, mantenimiento, usuario_id
        )

    def listar_mantenimientos(self):
        """
        Obtiene la lista de todos los mantenimientos registrados.

        Returns:
            list: Lista de mantenimientos.
        """
        
        return mantenimiento_crud.obtener_mantenimientos(self.db)
