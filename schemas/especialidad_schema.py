from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EspecialidadBase(BaseModel):
    """Esquema base para la entidad Especialidad."""

    nombre: str


class EspecialidadCreate(EspecialidadBase):
    """Esquema de entrada para la creación de especialidades."""

    pass


class EspecialidadOut(EspecialidadBase):
    """
    Esquema de salida para representar una especialidad en las respuestas de la API.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}
