from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AutoBase(BaseModel):
    marca: str
    modelo: str
    precio: float
    tipo: str
    extra: str | None = None


class AutoCreate(AutoBase):
    """Schema para crear autos"""

    pass


class AutoOut(AutoBase):
    id: UUID
    vendido: bool
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
