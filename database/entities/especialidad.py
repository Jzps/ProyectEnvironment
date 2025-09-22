import uuid
from sqlalchemy import Column, String, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base

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
    """
    Modelo ORM para la tabla ``especialidades``.

    Representa una especialidad técnica que un empleado de mantenimiento
    puede tener, como mecánica de motores o sistemas eléctricos.
    """

    __tablename__ = "especialidades"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    nombre = Column(String, unique=True, nullable=False)

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
