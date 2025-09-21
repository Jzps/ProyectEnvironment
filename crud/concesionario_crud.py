import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.concesionario import Concesionario
from schemas.concesionario_schema import ConcesionarioCreate
from uuid import UUID


def crear_concesionario(
    db: Session, concesionario: ConcesionarioCreate, usuario_id: UUID | None = None
):
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
    return db.query(Concesionario).all()
