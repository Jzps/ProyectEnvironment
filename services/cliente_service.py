from database.config import SessionLocal
from crud import cliente_crud
from schemas import ClienteCreate
from uuid import UUID


class ClienteService:
    """
    Servicio para manejar operaciones de clientes.

    Métodos: registrar, listar y eliminar clientes.
    Funciona como capa intermedia entre la BD y la lógica de negocio.
    """

    def __init__(self, db=None):
        """
        Constructor del servicio.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se pasa, se crea una nueva.
        """
        self.db = db or SessionLocal()

    def registrar_cliente(self, cliente: ClienteCreate, usuario_id: UUID | None = None):
        """
        Registra un cliente en la BD.

        Args:
            cliente (ClienteCreate): Datos del cliente.
            usuario_id (UUID | None): ID del usuario que lo crea (opcional).
        Returns:
            Cliente: Cliente creado.
        """
        return cliente_crud.crear_cliente(self.db, cliente, usuario_id)

    def listar_clientes(self):
        """
        Obtiene todos los clientes de la BD.

        Returns:
            list[Cliente]: Lista de clientes.
        """
        return cliente_crud.obtener_clientes(self.db)

    def eliminar_cliente(self, cliente_id: UUID):
        """
        Elimina un cliente por ID.

        Args:
            cliente_id (UUID): ID del cliente.
        Returns:
            Cliente | None: Cliente eliminado o None si no existe.
        """
        return cliente_crud.eliminar_cliente(self.db, cliente_id)
