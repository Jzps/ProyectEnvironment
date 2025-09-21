import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database.base import Base


class Admin(Base):
    """
    Modelo ORM para la tabla ``admins``.

    Representa a un administrador del sistema, con credenciales de acceso y
    metadatos de auditoría (quién creó o editó el registro y cuándo).

    Atributos
    ----------
    id : UUID
        Identificador único primario, generado automáticamente.
    username : str
        Nombre de usuario único del administrador.
    password : str
        Contraseña en formato seguro (hash o encriptada según la lógica de la aplicación).
    id_usuario_creacion : UUID | None
        Identificador del usuario que creó el registro, si corresponde.
    id_usuario_edicion : UUID | None
        Identificador del usuario que editó el registro por última vez, si corresponde.
    fecha_creacion : datetime
        Fecha y hora en que se creó el registro (UTC). Se asigna automáticamente.
    fecha_actualizacion : datetime
        Fecha y hora de la última actualización del registro (UTC).
        Se actualiza automáticamente en cada modificación.
    """
    
    __tablename__ = "admins"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

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
