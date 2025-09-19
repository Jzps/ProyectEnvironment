import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class EmpleadoMantenimiento(Base):
    __tablename__ = "empleados_mantenimiento"

    empleado_id = Column(
        UUID(as_uuid=True), ForeignKey("empleados.id"), primary_key=True
    )
    tipo_carro = Column(String, nullable=False)

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
