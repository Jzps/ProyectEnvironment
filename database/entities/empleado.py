import uuid
from sqlalchemy import Column, String, Date, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Empleado(Base):
    __tablename__ = "empleados"

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
    fecha_contratacion = Column(Date, nullable=False)

    concesionario_id = Column(
        UUID(as_uuid=True), ForeignKey("concesionarios.id"), nullable=True
    )

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
