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
    """
    Modelo ORM para la tabla ``facturas``.

    Representa una factura emitida por la venta de un auto. 
    Contiene la información de la transacción, incluyendo el
    cliente, el empleado vendedor, el vehículo vendido y los
    detalles de costos y descuentos.

    Restricciones
    -------------
    * ``uix_factura_auto_unico``: 
      Garantiza que cada auto pueda estar asociado como máximo
      a una sola factura (único por ``auto_id``).

    Atributos
    ----------
    id : UUID
        Identificador único de la factura.
        Clave primaria generada automáticamente con UUID v4.

    fecha_emision : date
        Fecha en que se emite la factura.

    cliente_id : UUID
        Llave foránea que referencia a ``clientes.id``.
        Identifica al cliente que realiza la compra.

    empleado_id : UUID
        Llave foránea que referencia a 
        ``empleados_vendedor.empleado_id``.
        Identifica al vendedor que gestionó la transacción.

    auto_id : UUID
        Llave foránea que referencia a ``autos.id``.
        Identifica el vehículo vendido.

    precio_carro_base : float
        Precio base del auto antes de mantenimiento, descuentos u otros cargos.

    costo_mantenimiento : float
        Costo total de mantenimientos asociados al vehículo
        antes de la venta. Por defecto 0.0.

    descuento : float
        Descuento aplicado a la venta. Por defecto 0.0.

    total : float
        Total final a pagar en la factura después de aplicar
        costos de mantenimiento y descuentos.

    observaciones : str | None
        Campo opcional para notas o comentarios adicionales.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro.

    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición.

    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro.
        Se asigna automáticamente al insertar la factura.

    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización.
        Se actualiza automáticamente en cada modificación.
    """
    
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

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
