from crud import admin_crud
from schemas.admin_schema import AdminCreate


class AdminService:
    def __init__(self, db):
        self.db = db

    def login(self, username: str, password: str):
        """
        Verifica si las credenciales son correctas.
        """
        admin = admin_crud.obtener_admin(self.db, username)
        if not admin:
            return False
        return admin.password == password

    def crear_admin(self, admin: AdminCreate):
        """
        Crea un nuevo administrador.
        """
        return admin_crud.crear_admin(self.db, admin)

    def listar_admins(self):
        """
        Devuelve la lista de todos los administradores registrados.
        """
        from database.entities.admin import (
            Admin,
        )

        return self.db.query(Admin).all()
