from database.config import SessionLocal
from crud import cliente_crud
from schemas import ClienteCreate
from uuid import UUID


class ClienteService:
    """
    Servicio para gestionar operaciones relacionadas con los clientes.

    Proporciona métodos para registrar, listar y eliminar clientes,
    actuando como capa intermedia entre la base de datos y la lógica de negocio.
    """

    def __init__(self, db=None):
        """
        Inicializa el servicio con una sesión de base de datos.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se proporciona, se crea una nueva.
        """

        self.db = db or SessionLocal()

    def registrar_cliente(self, cliente: ClienteCreate, usuario_id: UUID | None = None):
        """
        Registra un nuevo cliente en la base de datos.

        Args:
            cliente (ClienteCreate): Datos del cliente a registrar.
            usuario_id (UUID | None): ID del usuario que realiza la creación (opcional).

        Returns:
            Cliente: Objeto Cliente recién creado.
        """

        return cliente_crud.crear_cliente(self.db, cliente, usuario_id)

    def listar_clientes(self):
        """
        Retorna todos los clientes existentes en la base de datos.

        Returns:
            list[Cliente]: Lista de objetos Cliente.
        """

        return cliente_crud.obtener_clientes(self.db)

    def eliminar_cliente(self, cliente_id: UUID):
        """
        Elimina un cliente de la base de datos por su ID.

        Args:
            cliente_id (UUID): ID del cliente a eliminar.

        Returns:
            Cliente | None: Objeto Cliente eliminado si existía, o None si no se encontró.
        """
         
        return cliente_crud.eliminar_cliente(self.db, cliente_id)
