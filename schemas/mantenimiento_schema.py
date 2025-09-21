from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class MantenimientoBase(BaseModel):
    auto_id: UUID
    empleado_id: UUID
    fecha: date
    detalle: str
    costo: float


class MantenimientoCreate(MantenimientoBase):
    factura_id: UUID | None = None


class MantenimientoOut(MantenimientoBase):
    id: UUID
    factura_id: UUID | None = None
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
