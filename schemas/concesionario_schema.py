from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ConcesionarioBase(BaseModel):
    nombre: str
    ubicacion: str | None = None
    telefono: str | None = None


class ConcesionarioCreate(ConcesionarioBase):
    pass


class ConcesionarioOut(ConcesionarioBase):
    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
