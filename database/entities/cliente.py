import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Cliente(Base):
    """
    Modelo ORM para la tabla ``clientes``.

    Representa a un cliente del concesionario, incluyendo sus datos de
    identificación y contacto, así como la información de auditoría de
    creación y actualización del registro.

    Atributos
    ----------
    id : UUID
        Identificador único primario, generado automáticamente.
    nombre : str
        Nombre del cliente.
    apellido : str
        Apellido del cliente.
    dni : str
        Documento de identidad o número único de identificación.
        Debe ser único en la base de datos.
    correo : str | None
        Correo electrónico de contacto (opcional).
    telefono : str | None
        Número de teléfono de contacto (opcional).
    direccion : str | None
        Dirección de residencia o de contacto (opcional).

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si corresponde.
    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición, si corresponde.
    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro. Se asigna automáticamente.
    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización del registro.
        Se actualiza automáticamente en cada modificación; puede ser nula
        si nunca se ha editado.
    """
    
    __tablename__ = "clientes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    correo = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
