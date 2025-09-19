from crud import admin_crud
from schemas.admin_schema import AdminCreate
from uuid import UUID


class AdminService:
    def __init__(self, db):
        self.db = db

    def login(self, username: str, password: str):
        admin = admin_crud.obtener_admin(self.db, username)
        if not admin:
            return False
        return admin.password == password

    def crear_admin(self, admin: AdminCreate, usuario_id: UUID | None = None):
        return admin_crud.crear_admin(self.db, admin, usuario_id)

    def listar_admins(self):
        from database.entities.admin import Admin

        return self.db.query(Admin).all()
