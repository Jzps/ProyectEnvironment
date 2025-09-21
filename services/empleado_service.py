from database.config import SessionLocal
from crud import empleado_crud
from schemas import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate
from uuid import UUID


class EmpleadoService:
    """
    Servicio para gestionar empleados, vendedores y técnicos de mantenimiento.

    Proporciona métodos para registrar y listar empleados en sus diferentes roles,
    interactuando con el CRUD correspondiente.
    """

    def __init__(self, db=None):
        """
        Inicializa el servicio de empleados con una sesión de base de datos.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se proporciona, se crea una nueva.
        """
        
        self.db = db or SessionLocal()

    def registrar_empleado(
        self, empleado: EmpleadoCreate, usuario_id: UUID | None = None
    ):
        """
        Registra un nuevo empleado en la base de datos.

        Args:
            empleado (EmpleadoCreate): Datos del empleado a registrar.
            usuario_id (UUID | None): ID del usuario que realiza la creación.

        Returns:
            Empleado registrado en la base de datos.
        """

        return empleado_crud.crear_empleado(self.db, empleado, usuario_id)

    def listar_empleados(self):
        """
        Obtiene la lista de todos los empleados registrados.

        Returns:
            list: Lista de empleados.
        """

        return empleado_crud.obtener_empleados(self.db)

    def registrar_vendedor(
        self, vendedor: VendedorCreate, usuario_id: UUID | None = None
    ):
        """
        Registra a un empleado como vendedor.

        Args:
            vendedor (VendedorCreate): Datos del vendedor (empleado_id).
            usuario_id (UUID | None): ID del usuario que realiza la creación.

        Returns:
            Vendedor registrado en la base de datos.
        """

        return empleado_crud.registrar_vendedor(self.db, vendedor, usuario_id)

    def listar_vendedores(self):
        """
        Obtiene la lista de todos los empleados registrados como vendedores.

        Returns:
            list: Lista de vendedores.
        """
        
        return empleado_crud.obtener_vendedores(self.db)

    def registrar_tecnico(
        self, tecnico: MantenimientoEmpleadoCreate, usuario_id: UUID | None = None
    ):
        """
        Registra a un empleado como técnico de mantenimiento.

        Args:
            tecnico (MantenimientoEmpleadoCreate): Datos del técnico (empleado_id y tipo_carro).
            usuario_id (UUID | None): ID del usuario que realiza la creación.

        Returns:
            Técnico registrado en la base de datos.
        """

        return empleado_crud.registrar_mantenimiento_empleado(
            self.db, tecnico, usuario_id
        )

    def listar_tecnicos(self):
        """
        Obtiene la lista de todos los empleados registrados como técnicos de mantenimiento.

        Returns:
            list: Lista de técnicos.
        """
        
        return empleado_crud.obtener_tecnicos(self.db)
