from crud import admin_crud
from schemas.admin_schema import AdminCreate
from uuid import UUID


class AdminService:
    """
    Servicio para gestionar operaciones relacionadas con los administradores (Admin).

    Este servicio actúa como intermediario entre la capa de CRUD y la lógica de negocio,
    permitiendo realizar operaciones de creación, autenticación y listado de administradores.
    """

    def __init__(self, db):
        self.db = db

    def login(self, username: str, password: str):
        """
        Verifica las credenciales del administrador.

        Args:
            username (str): Usuario.
            password (str): Contraseña.
        Returns:
            bool: True si son válidas, False en caso contrario.
        """

        admin = admin_crud.obtener_admin(self.db, username)
        if not admin:
            return False
        return admin.password == password

    def crear_admin(self, admin: AdminCreate, usuario_id: UUID | None = None):
        """
        Crea un nuevo administrador en la base de datos.

        Args:
            admin (AdminCreate): Datos del administrador a crear.
            usuario_id (UUID | None): ID del usuario que realiza la creación (opcional).

        Returns:
            Admin: Objeto Admin recién creado.
        """

        return admin_crud.crear_admin(self.db, admin, usuario_id)

    def listar_admins(self):
        """
        Retorna todos los administradores existentes en la base de datos.

        Returns:
            list[Admin]: Lista de objetos Admin.
        """

        from database.entities.admin import Admin

        return self.db.query(Admin).all()
