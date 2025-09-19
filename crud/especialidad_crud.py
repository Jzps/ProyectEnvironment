import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.especialidad import Especialidad
from schemas.especialidad_schema import EspecialidadCreate
from uuid import UUID


def crear_especialidad(
    db: Session, especialidad: EspecialidadCreate, usuario_id: UUID | None = None
):
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
    return db.query(Especialidad).all()
