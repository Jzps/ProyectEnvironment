from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class MantenimientoBase(BaseModel):
    """
    Modelo base de Mantenimiento.
    Contiene auto, empleado, fecha, detalle y costo.
    """

    auto_id: UUID
    empleado_id: UUID
    fecha: date
    detalle: str
    costo: float


class MantenimientoCreate(MantenimientoBase):
    """
    Modelo de entrada para crear mantenimientos.
    Incluye factura_id opcional.
    """

    factura_id: UUID | None = None


class MantenimientoOut(MantenimientoBase):
    """
    Modelo de salida para mantenimientos.
    Incluye id, factura, usuarios de auditoría y fechas.
    """

    id: UUID
    factura_id: UUID | None = None
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """Permite conversión desde modelos ORM."""

        from_attributes = True
