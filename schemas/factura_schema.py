from pydantic import BaseModel
from datetime import date

class FacturaBase(BaseModel):
    fecha_emision: date
    cliente_id: int
    empleado_id: int
    auto_id: int
    precio_carro_base: float
    costo_mantenimiento: float = 0.0
    descuento: float = 0.0
    total: float
    observaciones: str | None = None

class FacturaCreate(FacturaBase):
    pass

class FacturaOut(FacturaBase):
    id: int

    class Config:
        orm_mode = True
