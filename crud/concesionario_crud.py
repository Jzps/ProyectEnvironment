import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.concesionario import Concesionario
from schemas.concesionario_schema import ConcesionarioCreate
from uuid import UUID


def crear_concesionario(
    db: Session, concesionario: ConcesionarioCreate, usuario_id: UUID | None = None
):
    """
    Crea un nuevo concesionario con los datos proporcionados.
    :param db: Sesión activa de SQLAlchemy.
    :param concesionario: Datos del concesionario a crear.
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :return: Objeto Concesionario recién creado.
    """
    db_concesionario = Concesionario(
        id=uuid.uuid4(),
        **concesionario.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_concesionario)
    db.commit()
    db.refresh(db_concesionario)
    return db_concesionario


def obtener_concesionarios(db: Session):
    """
    Retorna todos los concesionarios registrados en la base de datos.
    :param db: Sesión activa de SQLAlchemy.
    :return: Lista de objetos Concesionario.
    """
    return db.query(Concesionario).all()
