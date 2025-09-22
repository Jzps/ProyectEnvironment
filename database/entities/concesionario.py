import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Concesionario(Base):
    """
    Modelo ORM para la tabla ``concesionarios``.

    Representa una sucursal o punto de venta de la red de concesionarios,
    con información de identificación, contacto y datos de auditoría.

    Atributos
    ----------
    id : UUID
        Identificador único primario del concesionario, generado automáticamente.
    nombre : str
        Nombre oficial del concesionario o sucursal.
    ubicacion : str | None
        Dirección física o ubicación de la sucursal (opcional).
    telefono : str | None
        Número de teléfono de contacto (opcional).

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
    
    __tablename__ = "concesionarios"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
