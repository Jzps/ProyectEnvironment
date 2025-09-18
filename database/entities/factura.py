import uuid
from sqlalchemy import (
    Column,
    String,
    Float,
    Date,
    ForeignKey,
    UniqueConstraint,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Factura(Base):
    __tablename__ = "facturas"
    __table_args__ = (UniqueConstraint("auto_id", name="uix_factura_auto_unico"),)

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    fecha_emision = Column(Date, nullable=False)
    cliente_id = Column(UUID(as_uuid=True), ForeignKey("clientes.id"), nullable=False)
    empleado_id = Column(
        UUID(as_uuid=True), ForeignKey("empleados_vendedor.empleado_id"), nullable=False
    )
    auto_id = Column(UUID(as_uuid=True), ForeignKey("autos.id"), nullable=False)

    precio_carro_base = Column(Float, nullable=False)
    costo_mantenimiento = Column(Float, nullable=False, default=0.0)
    descuento = Column(Float, nullable=False, default=0.0)
    total = Column(Float, nullable=False)
    observaciones = Column(String, nullable=True)

    # Columnas de auditoría
    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
