from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AdminBase(BaseModel):
    username: str
    password: str


class AdminCreate(AdminBase):
    """Schema para crear un admin"""

    pass


class AdminOut(BaseModel):
    id: UUID
    username: str
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
