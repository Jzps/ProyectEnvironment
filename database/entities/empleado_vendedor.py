import uuid
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class EmpleadoVendedor(Base):
    """
    Modelo ORM para la tabla ``empleados_vendedor``.

    Representa la especialización de un empleado que trabaja en el
    área de ventas dentro del concesionario.  
    Contiene la relación con el empleado principal y los campos
    de auditoría para el control de creación y edición de registros.

    Atributos
    ----------
    empleado_id : UUID
        Identificador único del empleado vendedor.
        Clave primaria y llave foránea que referencia a ``empleados.id``.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si corresponde.

    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición, si corresponde.

    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro.
        Se asigna automáticamente al insertar el registro.

    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización del registro.
        Se actualiza automáticamente en cada modificación;
        puede ser nula si nunca se ha editado.
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
