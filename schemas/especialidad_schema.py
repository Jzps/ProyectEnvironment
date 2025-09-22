from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class EspecialidadBase(BaseModel):
    """
    Esquema base para la entidad Especialidad.

    Atributos:
        nombre (str): Nombre de la especialidad.
    """

    nombre: str


class EspecialidadCreate(EspecialidadBase):
    """
    Esquema de entrada para la creación de especialidades.

    Hereda de:
        EspecialidadBase: Incluye todos los campos necesarios para registrar una especialidad.
    """

    pass


class EspecialidadOut(EspecialidadBase):
    """
    Esquema de salida para representar una especialidad en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único de la especialidad.
        id_usuario_creacion (UUID | None): Identificador del usuario que creó el registro.
        id_usuario_edicion (UUID | None): Identificador del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para habilitar la conversión desde
        objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """

        from_attributes = True
