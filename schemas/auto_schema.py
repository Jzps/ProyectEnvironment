from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AutoBase(BaseModel):
    """
    Esquema base para la entidad Auto.
    """

    marca: str
    modelo: str
    precio: float
    tipo: str
    extra: str | None = None


class AutoCreate(AutoBase):
    """Esquema de entrada para la creación de un automóvil."""

    pass


class AutoOut(AutoBase):
    """
    Esquema de salida para representar un automóvil en las respuestas de la API.
    """

    id: UUID
    vendido: bool
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}
