from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ConcesionarioBase(BaseModel):
    """
    Esquema base para la entidad Concesionario.

    Atributos:
        nombre (str): Nombre del concesionario.
        ubicacion (str | None): Dirección o ubicación del concesionario (opcional).
        telefono (str | None): Número de contacto del concesionario (opcional).
    """

    nombre: str
    ubicacion: str | None = None
    telefono: str | None = None


class ConcesionarioCreate(ConcesionarioBase):
    """
    Esquema de entrada para la creación de concesionarios.

    Hereda de:
        ConcesionarioBase: Incluye todos los campos necesarios para registrar un concesionario.
    """

    pass


class ConcesionarioOut(ConcesionarioBase):
    """
    Esquema de salida para representar un concesionario en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del concesionario.
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
        objetos ORM (por ejemplo, instancias de SQLAlchemy) a este esquema.
        """

        from_attributes = True
