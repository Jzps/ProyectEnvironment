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

    Args:
        db (Session): Sesión activa de SQLAlchemy.
        concesionario (ConcesionarioCreate): Datos del concesionario a crear.
        usuario_id (UUID | None): ID del usuario que crea el registro (opcional).

    Returns:
        Concesionario: Objeto Concesionario recién creado.
    """
    db_concesionario = Concesionario(
        id=uuid.uuid4(),
        nombre=concesionario.nombre,
        direccion=concesionario.direccion,
        telefono=concesionario.telefono,
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

    Args:
        db (Session): Sesión activa de SQLAlchemy.

    Returns:
        list[Concesionario]: Lista de objetos Concesionario.
    """
    return db.query(Concesionario).all()


def actualizar_concesionario(
    db: Session, concesionario_id: UUID, concesionario: ConcesionarioCreate
):
    db_concesionario = (
        db.query(Concesionario).filter(Concesionario.id == concesionario_id).first()
    )
    if db_concesionario:
        for key, value in concesionario.dict().items():
            setattr(db_concesionario, key, value)
        db.commit()
        db.refresh(db_concesionario)
    return db_concesionario
