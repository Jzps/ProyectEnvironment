from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class FacturaBase(BaseModel):
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
    pass


class FacturaOut(FacturaBase):
    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
