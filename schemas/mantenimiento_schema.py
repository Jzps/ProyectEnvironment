"""
Esquemas Pydantic para la entidad Mantenimiento.

Incluye modelos para:
- Validación de datos de entrada al registrar un mantenimiento.
- Representación de la información del mantenimiento en las respuestas de la API.
"""

from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class MantenimientoBase(BaseModel):
    """
    Esquema base para la entidad Mantenimiento.

    Atributos:
        auto_id (UUID): Identificador del auto que recibe el mantenimiento.
        empleado_id (UUID): Identificador del técnico o empleado que realiza el mantenimiento.
        fecha (date): Fecha en que se realizó el mantenimiento.
        detalle (str): Descripción detallada del mantenimiento.
        costo (float): Costo asociado al mantenimiento.
    """

    auto_id: UUID
    empleado_id: UUID
    fecha: date
    detalle: str
    costo: float


class MantenimientoCreate(MantenimientoBase):
    """
    Esquema para la creación de un mantenimiento.

    Atributos adicionales:
        factura_id (UUID | None, opcional): Identificador de la factura asociada al mantenimiento.
    """

    factura_id: UUID | None = None


class MantenimientoOut(MantenimientoBase):
    """
    Esquema de salida para representar la información de un mantenimiento
    en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del mantenimiento.
        factura_id (UUID | None): Identificador de la factura asociada, si aplica.
        id_usuario_creacion (UUID | None): ID del usuario que creó el registro.
        id_usuario_edicion (UUID | None): ID del usuario que realizó la última modificación.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización del registro.
    """

    id: UUID
    factura_id: UUID | None = None
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
