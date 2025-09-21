"""
Esquemas Pydantic para la entidad Especialidad.

Incluye modelos para:
- Validación de datos de entrada al crear una especialidad.
- Representación de la información de la especialidad en las respuestas de la API.
"""

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
    Esquema para la creación de una especialidad.

    Hereda:
        EspecialidadBase: Incluye todos los campos necesarios para registrar una especialidad.
    """
     
    pass


class EspecialidadOut(EspecialidadBase):
    """
    Esquema de salida para representar la información de una especialidad
    en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único de la especialidad.
        id_usuario_creacion (UUID | None): ID del usuario que creó el registro.
        id_usuario_edicion (UUID | None): ID del usuario que realizó la última modificación.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización del registro.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para permitir la conversión
        desde objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """
        
        from_attributes = True
