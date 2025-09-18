import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Concesionario(Base):
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

    # Columnas de auditoría
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
