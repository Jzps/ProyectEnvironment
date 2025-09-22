from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ClienteBase(BaseModel):
    """
    Esquema base para la entidad Cliente.

    Atributos:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        dni (str): Documento de identidad del cliente.
        correo (str | None): Correo electrónico del cliente (opcional).
        telefono (str | None): Número de teléfono del cliente (opcional).
        direccion (str | None): Dirección de residencia del cliente (opcional).
    """

    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    direccion: str | None = None


class ClienteCreate(ClienteBase):
    """
    Esquema de entrada para la creación de clientes.

    Hereda de:
        ClienteBase: Incluye todos los campos necesarios para registrar un cliente.
    """

    pass


class ClienteOut(ClienteBase):
    """
    Esquema de salida para representar un cliente en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del cliente.
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
