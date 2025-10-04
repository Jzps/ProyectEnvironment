from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ClienteBase(BaseModel):
    """
    Esquema base para la entidad Cliente.
    """

    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    direccion: str | None = None


class ClienteCreate(ClienteBase):
    """Esquema de entrada para la creación de clientes."""

    pass


class ClienteOut(ClienteBase):
    """
    Esquema de salida para representar un cliente en las respuestas de la API.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}
