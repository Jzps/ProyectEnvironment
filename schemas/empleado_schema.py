from pydantic import BaseModel
from datetime import date


class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    fecha_contratacion: date | None = None
    concesionario_id: int | None = None


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoOut(EmpleadoBase):
    id: int

    class Config:
        orm_mode = True


class VendedorCreate(BaseModel):
    empleado_id: int


class VendedorOut(BaseModel):
    empleado_id: int

    class Config:
        orm_mode = True


class MantenimientoEmpleadoCreate(BaseModel):
    empleado_id: int
    tipo_carro: str


class MantenimientoEmpleadoOut(MantenimientoEmpleadoCreate):
    class Config:
        orm_mode = True
