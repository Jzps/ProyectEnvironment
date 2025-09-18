import uuid
from sqlalchemy import Column, String, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database.base import Base
from datetime import datetime

# Tabla intermedia para relación muchos a muchos
empleado_mantenimiento_especialidad = Table(
    "empleado_mantenimiento_especialidad",
    Base.metadata,
    Column(
        "empleado_id",
        UUID(as_uuid=True),
        ForeignKey("empleados_mantenimiento.empleado_id"),
        primary_key=True,
    ),
    Column(
        "especialidad_id",
        UUID(as_uuid=True),
        ForeignKey("especialidades.id"),
        primary_key=True,
    ),
)


class Especialidad(Base):
    __tablename__ = "especialidades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String, unique=True, nullable=False)

    # columnas de auditoría
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
