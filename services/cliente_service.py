from database.config import SessionLocal
from crud import cliente_crud
from schemas import ClienteCreate


class ClienteService:
    def __init__(self, db=None):
        if db is None:
            self.db = SessionLocal()
        else:
            self.db = db

    def registrar_cliente(self, cliente: ClienteCreate):
        return cliente_crud.crear_cliente(self.db, cliente)

    def listar_clientes(self):
        return cliente_crud.obtener_clientes(self.db)

    def eliminar_cliente(self, cliente_id: int):
        return cliente_crud.eliminar_cliente(self.db, cliente_id)
