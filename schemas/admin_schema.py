from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AdminBase(BaseModel):
    """Datos base de un administrador (usuario y contraseña)."""

    username: str
    password: str


class AdminCreate(AdminBase):
    """Esquema para crear un administrador (hereda de AdminBase)."""

    pass


class AdminOut(BaseModel):
    """Esquema de salida de administrador con metadatos de creación y actualización."""

    id: UUID
    username: str
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}
