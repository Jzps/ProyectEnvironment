import uuid
from sqlalchemy import Boolean, Column, Float, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Auto(Base):
    """
    Modelo ORM para la tabla ``autos``.

    Representa un automóvil registrado en el concesionario, con información
    de su modelo, precio y estado de venta. Incluye además campos de auditoría
    para rastrear la creación y actualización del registro.

    Atributos
    ----------
    id : UUID
        Identificador único primario, generado automáticamente.
    marca : str
        Marca del vehículo (por ejemplo, Toyota, Ford).
    modelo : str
        Modelo específico del vehículo (por ejemplo, Corolla, Focus).
    precio : float
        Precio de venta del automóvil.
    tipo : str
        Tipo de automóvil (por ejemplo, sedán, SUV, eléctrico).
    extra : str | None
        Información adicional o características especiales (puede ser nula).
    vendido : bool
        Indica si el auto ya fue vendido. Por defecto es False.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si corresponde.
    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición, si corresponde.
    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro. Se asigna automáticamente.
    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización. Se actualiza automáticamente
        en cada modificación; puede ser nula si nunca se ha editado.
    """
    
    __tablename__ = "autos"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    marca = Column(String, index=True, nullable=False)
    modelo = Column(String, index=True, nullable=False)
    precio = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    extra = Column(String, nullable=True)
    vendido = Column(Boolean, default=False)

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
