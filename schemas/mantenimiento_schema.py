from pydantic import BaseModel
from datetime import date


class MantenimientoBase(BaseModel):
    auto_id: int
    empleado_id: int
    fecha: date
    detalle: str
    costo: float


class MantenimientoCreate(MantenimientoBase):
    factura_id: int | None = None


class MantenimientoOut(MantenimientoBase):
    id: int
    factura_id: int | None = None

    class Config:
        orm_mode = True
