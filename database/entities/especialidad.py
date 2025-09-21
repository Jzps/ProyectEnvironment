import uuid
from sqlalchemy import Column, String, Table, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base

"""
    Tabla de asociación para la relación muchos-a-muchos entre
    empleados de mantenimiento y especialidades.

    Esta tabla intermedia vincula a cada empleado de mantenimiento
    con las distintas especialidades en las que está capacitado.

    Columnas
    --------
    empleado_id : UUID
        Identificador del empleado de mantenimiento.
        Llave foránea que referencia a
        ``empleados_mantenimiento.empleado_id``.
        Clave primaria compuesta.

    especialidad_id : UUID
        Identificador de la especialidad.
        Llave foránea que referencia a ``especialidades.id``.
        Clave primaria compuesta.
    """

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

    Representa una especialidad o área técnica que un empleado de
    mantenimiento puede tener, como por ejemplo mecánica de motores,
    sistemas eléctricos, aire acondicionado, etc.

    Atributos
    ----------
    id : UUID
        Identificador único de la especialidad.
        Clave primaria generada automáticamente con UUID v4.

    nombre : str
        Nombre único que identifica la especialidad.

    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro.

    id_usuario_edicion : UUID | None
        Identificador del usuario que realizó la última edición.

    fecha_creacion : datetime
        Fecha y hora (UTC) en que se creó el registro.
        Se asigna automáticamente en la inserción.

    fecha_actualizacion : datetime
        Fecha y hora (UTC) de la última actualización.
        Se actualiza automáticamente en cada modificación.
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
