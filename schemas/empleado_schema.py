from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    fecha_contratacion: date | None = None
    concesionario_id: UUID | None = None


class EmpleadoCreate(EmpleadoBase):
    pass


class EmpleadoOut(EmpleadoBase):
    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True


class VendedorCreate(BaseModel):
    empleado_id: UUID


class VendedorOut(BaseModel):
    empleado_id: UUID

    class Config:
        from_attributes = True


class MantenimientoEmpleadoCreate(BaseModel):
    empleado_id: UUID
    tipo_carro: str


class MantenimientoEmpleadoOut(MantenimientoEmpleadoCreate):
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        from_attributes = True
