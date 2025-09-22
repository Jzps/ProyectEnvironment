"""
Esquemas Pydantic para la entidad Factura.

Incluye modelos para:
- Validación de datos de entrada al crear una factura.
- Representación de la información de la factura en las respuestas de la API.
"""

from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class FacturaBase(BaseModel):
    """
    Esquema base para la entidad Factura.

    Atributos:
        fecha_emision (date): Fecha de emisión de la factura.
        cliente_id (UUID): Identificador del cliente asociado.
        empleado_id (UUID): Identificador del empleado vendedor asociado.
        auto_id (UUID): Identificador del auto vendido.
        precio_carro_base (float): Precio base del auto.
        costo_mantenimiento (float, opcional): Costo de mantenimiento incluido en la factura. Por defecto 0.0.
        descuento (float, opcional): Descuento aplicado. Por defecto 0.0.
        total (float): Total de la factura considerando precio, mantenimiento y descuentos.
        observaciones (str | None, opcional): Comentarios adicionales de la factura.
    """

    fecha_emision: date
    cliente_id: UUID
    empleado_id: UUID
    auto_id: UUID
    precio_carro_base: float
    costo_mantenimiento: float = 0.0
    descuento: float = 0.0
    total: float
    observaciones: str | None = None


class FacturaCreate(FacturaBase):
    """
    Esquema para la creación de una factura.

    Hereda:
        FacturaBase: Incluye todos los campos necesarios para registrar una factura.
    """
    pass


class FacturaOut(FacturaBase):
    """
    Esquema de salida para representar la información de una factura
    en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único de la factura.
        id_usuario_creacion (UUID | None): ID del usuario que creó la factura.
        id_usuario_edicion (UUID | None): ID del usuario que realizó la última modificación.
        fecha_creacion (datetime | None): Fecha y hora de creación de la factura.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización de la factura.
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
