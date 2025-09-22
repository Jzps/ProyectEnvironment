from database.config import SessionLocal
from crud import empleado_crud
from schemas import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate
from uuid import UUID


class EmpleadoService:
    """
    Servicio para gestionar empleados y sus roles (vendedor o técnico).

    Actúa como capa intermedia entre la base de datos y la lógica de negocio,
    ofreciendo métodos para registrar y consultar empleados.
    """

    def __init__(self, db=None):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se proporciona, se crea una nueva.
        """

        self.db = db or SessionLocal()

    def registrar_empleado(
        self, empleado: EmpleadoCreate, usuario_id: UUID | None = None
    ):
        """
        Crea un nuevo empleado en la base de datos.
        """
        return empleado_crud.crear_empleado(self.db, empleado, usuario_id)

    def listar_empleados(self):
        """Devuelve todos los empleados registrados."""
        return empleado_crud.obtener_empleados(self.db)

    def registrar_vendedor(
        self, vendedor: VendedorCreate, usuario_id: UUID | None = None
    ):
        """
        Asigna el rol de vendedor a un empleado existente.
        """
        return empleado_crud.registrar_vendedor(self.db, vendedor, usuario_id)

    def listar_vendedores(self):
        """Devuelve la lista de empleados con rol de vendedor."""
        return empleado_crud.obtener_vendedores(self.db)

    def registrar_tecnico(
        self, tecnico: MantenimientoEmpleadoCreate, usuario_id: UUID | None = None
    ):
        """
        Asigna el rol de técnico de mantenimiento a un empleado.
        """
        return empleado_crud.registrar_mantenimiento_empleado(
            self.db, tecnico, usuario_id
        )

    def listar_tecnicos(self):
        """Devuelve la lista de empleados con rol de técnico de mantenimiento."""
        return empleado_crud.obtener_tecnicos(self.db)
