from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class FacturaBase(BaseModel):
    """
    Modelo base de Factura.
    Contiene datos comunes como fecha, cliente, empleado, auto, precios y observaciones.
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
    Modelo de entrada para crear facturas.
    Hereda de FacturaBase.
    """

    pass


class FacturaOut(FacturaBase):
    """
    Modelo de salida para facturas.
    Incluye id, usuarios de creación/edición y fechas de registro.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """Permite la conversión desde objetos ORM."""

        from_attributes = True
