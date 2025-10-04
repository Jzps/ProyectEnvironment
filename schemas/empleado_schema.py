from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class EmpleadoBase(BaseModel):
    """
    Esquema base para la entidad Empleado.
    """

    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    fecha_contratacion: date | None = None
    concesionario_id: UUID | None = None


class EmpleadoCreate(EmpleadoBase):
    """Esquema de entrada para la creación de empleados."""

    pass


class EmpleadoOut(EmpleadoBase):
    """
    Esquema de salida para representar un empleado en las respuestas de la API.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}


class VendedorCreate(BaseModel):
    """
    Esquema de entrada para la creación de registros de vendedores.
    """

    empleado_id: UUID


class VendedorOut(BaseModel):
    """
    Esquema de salida para representar un registro de vendedor.
    """

    empleado_id: UUID

    model_config = {"from_attributes": True}


class MantenimientoEmpleadoCreate(BaseModel):
    """
    Esquema de entrada para la creación de empleados de mantenimiento.
    """

    empleado_id: UUID
    tipo_carro: str


class MantenimientoEmpleadoOut(MantenimientoEmpleadoCreate):
    """
    Esquema de salida para representar un empleado de mantenimiento.
    """

    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    model_config = {"from_attributes": True}
