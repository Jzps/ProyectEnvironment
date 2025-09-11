from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate

def crear_auto(db: Session, auto: AutoCreate):
    db_auto = Auto(
        marca=auto.marca,
        modelo=auto.modelo,
        precio=auto.precio,
        tipo=auto.tipo,
        extra=auto.extra
    )
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto

def obtener_autos(db: Session):
    return db.query(Auto).all()

def eliminar_auto(db: Session, auto_id: int):
    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
    return auto
