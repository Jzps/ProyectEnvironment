import uuid
from sqlalchemy import Column, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    auto_id = Column(UUID(as_uuid=True), ForeignKey("autos.id"), nullable=False)
    empleado_id = Column(
        UUID(as_uuid=True),
        ForeignKey("empleados_mantenimiento.empleado_id"),
        nullable=False,
    )
    fecha = Column(Date, nullable=False)
    detalle = Column(String, nullable=False)
    costo = Column(Float, nullable=False)
    factura_id = Column(UUID(as_uuid=True), ForeignKey("facturas.id"), nullable=True)

    # Columnas de auditoría
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
