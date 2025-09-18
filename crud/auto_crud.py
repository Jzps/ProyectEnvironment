import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate
from uuid import UUID


def crear_auto(db: Session, auto: AutoCreate, usuario_id: UUID | None = None):
    db_auto = Auto(
        id=uuid.uuid4(),
        marca=auto.marca,
        modelo=auto.modelo,
        precio=auto.precio,
        tipo=auto.tipo,
        extra=auto.extra,
        vendido=False,
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto


def obtener_autos(db: Session, disponibles_only: bool = True):
    q = db.query(Auto)
    if disponibles_only:
        q = q.filter(Auto.vendido == False)
    return q.all()


def obtener_auto_por_id(db: Session, auto_id: UUID):
    return db.query(Auto).filter(Auto.id == auto_id).first()


def marcar_vendido(db: Session, auto_id: UUID, usuario_id: UUID | None = None):
    auto_obj = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto_obj:
        auto_obj.vendido = True
        auto_obj.id_usuario_edicion = usuario_id
        auto_obj.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(auto_obj)
    return auto_obj


def eliminar_auto(db: Session, auto_id: UUID):
    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
    return auto


def obtener_autos_vendidos(db: Session):
    return db.query(Auto).filter(Auto.vendido == True).all()
