import uuid
from sqlalchemy import Boolean, Column, Float, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Auto(Base):
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

    # Columnas de auditoría
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
