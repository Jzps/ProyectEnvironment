from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID


class EmpleadoBase(BaseModel):
    """
    Esquema base para la entidad Empleado.

    Atributos:
        nombre (str): Nombre del empleado.
        apellido (str): Apellido del empleado.
        dni (str): Documento de identidad del empleado.
        correo (str | None): Correo electrónico del empleado (opcional).
        telefono (str | None): Número de teléfono de contacto (opcional).
        fecha_contratacion (date | None): Fecha de contratación del empleado (opcional).
        concesionario_id (UUID | None): Identificador del concesionario donde trabaja (opcional).
    """

    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    fecha_contratacion: date | None = None
    concesionario_id: UUID | None = None


class EmpleadoCreate(EmpleadoBase):
    """
    Esquema de entrada para la creación de empleados.

    Hereda de:
        EmpleadoBase: Incluye todos los campos necesarios para registrar un empleado.
    """

    pass


class EmpleadoOut(EmpleadoBase):
    """
    Esquema de salida para representar un empleado en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del empleado.
        id_usuario_creacion (UUID | None): Identificador del usuario que creó el registro.
        id_usuario_edicion (UUID | None): Identificador del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id: UUID
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para habilitar la conversión desde
        objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """

        from_attributes = True


class VendedorCreate(BaseModel):
    """
    Esquema de entrada para la creación de registros de vendedores.

    Atributos:
        empleado_id (UUID): Identificador del empleado que será marcado como vendedor.
    """

    empleado_id: UUID


class VendedorOut(BaseModel):
    """
    Esquema de salida para representar un registro de vendedor.

    Atributos:
        empleado_id (UUID): Identificador del empleado asociado como vendedor.
    """

    empleado_id: UUID

    class Config:
        """
        Configuración de Pydantic para habilitar la conversión desde
        objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """

        from_attributes = True


class MantenimientoEmpleadoCreate(BaseModel):
    """
    Esquema de entrada para la creación de empleados de mantenimiento.

    Atributos:
        empleado_id (UUID): Identificador del empleado asignado al mantenimiento.
        tipo_carro (str): Tipo o categoría de vehículos en los que está especializado.
    """

    empleado_id: UUID
    tipo_carro: str


class MantenimientoEmpleadoOut(MantenimientoEmpleadoCreate):
    """
    Esquema de salida para representar un empleado de mantenimiento.

    Atributos adicionales:
        id_usuario_creacion (UUID | None): Identificador del usuario que creó el registro.
        id_usuario_edicion (UUID | None): Identificador del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para habilitar la conversión desde
        objetos ORM (por ejemplo, modelos de SQLAlchemy).
        """

        from_attributes = True
