import uuid
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class EmpleadoVendedor(Base):
    """
    Modelo ORM para la tabla ``empleados_vendedor``.

    Representa la especialización de un empleado en el área de ventas,
    vinculada al registro principal de empleados e incluyendo datos de auditoría.
    """

    __tablename__ = "empleados_vendedor"

    empleado_id = Column(
        UUID(as_uuid=True), ForeignKey("empleados.id"), primary_key=True
    )

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
