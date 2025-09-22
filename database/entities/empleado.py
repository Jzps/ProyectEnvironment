import uuid
from sqlalchemy import Column, String, Date, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Empleado(Base):
    """
    Modelo ORM para la tabla ``empleados``.

    Representa a un empleado del concesionario, ya sea del área de
    ventas o de mantenimiento.  
    Incluye datos personales, fecha de contratación, y una posible
    relación con un concesionario específico, junto con los campos de
    auditoría para control de creación y modificación de registros.

    Atributos
    ----------
    id : UUID
        Identificador único del empleado.
        Clave primaria generada automáticamente con UUID v4.

    nombre : str
        Nombres del empleado.

    apellido : str
        Apellidos del empleado.

    dni : str
        Documento de identidad único del empleado.
        Campo obligatorio y único en la base de datos.

    correo : str | None
        Correo electrónico de contacto (opcional).

    telefono : str | None
        Número de teléfono del empleado (opcional).

    fecha_contratacion : date
        Fecha en que el empleado fue contratado.

    concesionario_id : UUID | None
        Identificador del concesionario al que pertenece el empleado.
        Llave foránea que referencia a ``concesionarios.id``.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si aplica.

    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición,
        si aplica.

    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro.
        Se asigna automáticamente en la inserción.

    fecha_actualizacion : datetime | None
        Fecha y hora (UTC) de la última actualización.
        Se actualiza automáticamente en cada modificación; puede ser
        nula si nunca se ha editado.
    """
    
    __tablename__ = "empleados"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    correo = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    fecha_contratacion = Column(Date, nullable=False)

    concesionario_id = Column(
        UUID(as_uuid=True), ForeignKey("concesionarios.id"), nullable=True
    )

    id_usuario_creacion = Column(UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
