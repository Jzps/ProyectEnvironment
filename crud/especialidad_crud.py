from sqlalchemy.orm import Session
from database.entities.especialidad import Especialidad
from schemas.especialidad_schema import EspecialidadCreate

def crear_especialidad(db: Session, especialidad: EspecialidadCreate):
    db_especialidad = Especialidad(**especialidad.dict())
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad

def obtener_especialidades(db: Session):
    return db.query(Especialidad).all()