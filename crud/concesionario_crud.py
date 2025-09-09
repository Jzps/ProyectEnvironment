from sqlalchemy.orm import Session
from database.entities.concesionario import Concesionario
from schemas.concesionario_schema import ConcesionarioCreate

def crear_concesionario(db: Session, concesionario: ConcesionarioCreate):
    db_concesionario = Concesionario(**concesionario.dict())
    db.add(db_concesionario)
    db.commit()
    db.refresh(db_concesionario)
    return db_concesionario

def obtener_concesionarios(db: Session):
    return db.query(Concesionario).all()