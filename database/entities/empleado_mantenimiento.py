import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class EmpleadoMantenimiento(Base):
    """
    Modelo ORM para la tabla ``empleados_mantenimiento``.

    Representa a un empleado especializado en el área de mantenimiento
    de vehículos, indicando el tipo de carros que atiende y datos de
    auditoría de creación y actualización.

    Atributos
    ----------
    empleado_id : UUID
        Identificador único del empleado, clave primaria y
        llave foránea que referencia a ``empleados.id``.
    tipo_carro : str
        Tipo de vehículo en el que el empleado está especializado
        para realizar mantenimiento (por ejemplo: "eléctrico", "diésel",
        "gasolina", "híbrido").

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si corresponde.
    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición, si corresponde.
    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro. Se asigna automáticamente.
    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización del registro.
        Se actualiza automáticamente en cada modificación; puede ser nula
        si nunca se ha editado.
    """
    
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
