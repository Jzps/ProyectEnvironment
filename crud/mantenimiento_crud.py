from sqlalchemy.orm import Session
from database.entities.mantenimiento import Mantenimiento
from schemas.mantenimiento_schema import MantenimientoCreate

def registrar_mantenimiento(db: Session, mantenimiento: MantenimientoCreate):
    db_mantenimiento = Mantenimiento(**mantenimiento.dict())
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)
    return db_mantenimiento

def obtener_mantenimientos(db: Session):
    return db.query(Mantenimiento).all()