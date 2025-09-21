"""
Esquemas Pydantic para la entidad Auto.

Define los modelos de datos para validar la creación de autos y
para la representación de salida en las respuestas de la API.
"""

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AutoBase(BaseModel):
    """
    Esquema base para la entidad Auto.

    Atributos:
        marca (str): Marca del automóvil.
        modelo (str): Modelo del automóvil.
        precio (float): Precio del automóvil.
        tipo (str): Tipo o categoría del automóvil (por ejemplo, eléctrico, usado, etc.).
        extra (str | None): Información adicional u opcional del auto.
    """

    marca: str
    modelo: str
    precio: float
    tipo: str
    extra: str | None = None


class AutoCreate(AutoBase):
    """
    Esquema de datos para la creación de un automóvil.

    Hereda de:
        AutoBase: Incluye todos los campos básicos necesarios para crear un auto.
    """

    pass


class AutoOut(AutoBase):
    """
    Esquema de salida para representar un automóvil en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del auto.
        vendido (bool): Indica si el auto ya fue vendido.
        id_usuario_creacion (UUID | None): ID del usuario que creó el registro.
        id_usuario_edicion (UUID | None): ID del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id: UUID
    vendido: bool
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para permitir la conversión desde
        objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """
        
        from_attributes = True
