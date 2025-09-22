from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AdminBase(BaseModel):
    """
    Esquema base para la entidad de administrador.

    Atributos:
        username (str): Nombre de usuario único del administrador.
        password (str): Contraseña en texto plano (normalmente se encripta antes de guardar).
    """

    username: str
    password: str


class AdminCreate(AdminBase):
    """
    Esquema de datos para la creación de un administrador.

    Hereda de:
        AdminBase: incluye los campos username y password.
    """

    pass


class AdminOut(BaseModel):
    """
    Esquema de salida para representar un administrador en las respuestas de la API.

    Atributos:
        id (UUID): Identificador único del administrador.
        username (str): Nombre de usuario del administrador.
        id_usuario_creacion (UUID | None): ID del usuario que creó el registro.
        id_usuario_edicion (UUID | None): ID del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id: UUID
    username: str
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para permitir la creación del esquema
        a partir de objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """
        
        from_attributes = True
