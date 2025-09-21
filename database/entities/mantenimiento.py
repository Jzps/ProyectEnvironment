import uuid
from sqlalchemy import Column, String, Float, Date, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Mantenimiento(Base):
    """
    Modelo ORM para la tabla ``mantenimientos``.

    Registra las operaciones de mantenimiento realizadas
    a un automóvil, indicando el técnico que las ejecutó,
    los costos asociados y su posible vínculo a una factura.

    Atributos
    ----------
    id : UUID
        Identificador único del mantenimiento.
        Clave primaria generada automáticamente (UUID v4).

    auto_id : UUID
        Llave foránea que referencia a ``autos.id``.
        Identifica el vehículo que recibe el mantenimiento.

    empleado_id : UUID
        Llave foránea que referencia a 
        ``empleados_mantenimiento.empleado_id``.
        Identifica al empleado técnico que realiza el mantenimiento.

    fecha : date
        Fecha en que se efectúa la intervención de mantenimiento.

    detalle : str
        Descripción de las tareas o trabajos realizados.

    costo : float
        Costo total del mantenimiento realizado.

    factura_id : UUID | None
        Llave foránea que referencia a ``facturas.id``.
        Si el mantenimiento se incluye en una factura,
        este campo enlaza con la misma; puede ser nulo.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro.

    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición.

    fecha_creacion : datetime
        Fecha y hora (UTC) en la que se creó el registro.
        Se asigna automáticamente al insertar.

    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última modificación.
        Se actualiza automáticamente en cada edición.
    """
    
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
