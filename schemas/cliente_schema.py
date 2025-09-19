from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    direccion: str | None = None


class ClienteCreate(ClienteBase):
    """Schema para crear clientes"""

    pass


class ClienteOut(ClienteBase):
    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
