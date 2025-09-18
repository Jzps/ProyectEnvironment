from database.config import SessionLocal
from crud import cliente_crud
from schemas import ClienteCreate
from uuid import UUID


class ClienteService:
    def __init__(self, db=None):
        self.db = db or SessionLocal()

    def registrar_cliente(self, cliente: ClienteCreate, usuario_id: UUID | None = None):
        return cliente_crud.crear_cliente(self.db, cliente, usuario_id)

    def listar_clientes(self):
        return cliente_crud.obtener_clientes(self.db)

    def eliminar_cliente(self, cliente_id: UUID):
        return cliente_crud.eliminar_cliente(self.db, cliente_id)
