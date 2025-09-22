import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.especialidad import Especialidad
from schemas.especialidad_schema import EspecialidadCreate
from uuid import UUID


def crear_especialidad(
    db: Session, especialidad: EspecialidadCreate, usuario_id: UUID | None = None
):
    """
    Crea una nueva especialidad en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param especialidad: Datos para la creación de la especialidad.
    :type especialidad: schemas.especialidad_schema.EspecialidadCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Especialidad recién creado.
    :rtype: database.entities.especialidad.Especialidad
    """

    db_especialidad = Especialidad(
        id=uuid.uuid4(),
        **especialidad.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad


def obtener_especialidades(db: Session):
    """
    Obtiene todas las especialidades registradas en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos Especialidad.
    :rtype: list[database.entities.especialidad.Especialidad]
    """

    return db.query(Especialidad).all()
