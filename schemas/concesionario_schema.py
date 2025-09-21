"""
Esquemas Pydantic para la entidad Concesionario.

Proporciona modelos para:
- Validar los datos de entrada al crear un concesionario.
- Representar la información de salida en las respuestas de la API.
"""

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ConcesionarioBase(BaseModel):
    """
    Esquema base para la entidad Concesionario.

    Atributos:
        nombre (str): Nombre del concesionario.
        ubicacion (str | None): Dirección o ubicación del concesionario (opcional).
        telefono (str | None): Número de contacto del concesionario (opcional).
    """

    nombre: str
    ubicacion: str | None = None
    telefono: str | None = None


class ConcesionarioCreate(ConcesionarioBase):
    """
    Esquema para la creación de un concesionario.

    Hereda de:
        ConcesionarioBase: Incluye todos los campos necesarios para registrar un concesionario.
    """

    pass


class ConcesionarioOut(ConcesionarioBase):
    """
    Esquema de salida para representar la información de un concesionario en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del concesionario.
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
