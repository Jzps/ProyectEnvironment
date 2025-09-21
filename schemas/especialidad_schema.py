from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EspecialidadBase(BaseModel):
    nombre: str


class EspecialidadCreate(EspecialidadBase):
    pass


class EspecialidadOut(EspecialidadBase):
    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
