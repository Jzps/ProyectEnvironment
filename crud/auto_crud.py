from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate


def crear_auto(db: Session, auto: AutoCreate):
    """
    Crea un auto; por defecto `vendido` es False.
    """
    db_auto = Auto(
        marca=auto.marca,
        modelo=auto.modelo,
        precio=auto.precio,
        tipo=auto.tipo,
        extra=auto.extra,
        vendido=False,
    )
    db.add(db_auto)
    db.commit()
    db.refresh(db_auto)
    return db_auto


def obtener_autos(db: Session, disponibles_only: bool = True):
    """
    Obtiene autos. Por defecto devuelve solo los disponibles (vendido == False).
    Si disponibles_only=False devuelve todos los autos.
    """
    q = db.query(Auto)
    if disponibles_only:
        q = q.filter(Auto.vendido == False)
    return q.all()


def obtener_auto_por_id(db: Session, auto_id: int):
    return db.query(Auto).filter(Auto.id == auto_id).first()


def marcar_vendido(db: Session, auto_id: int):
    """
    Marca un auto como vendido (vendido=True). Devuelve el objeto actualizado.
    """
    auto_obj = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto_obj:
        auto_obj.vendido = True
        db.commit()
        db.refresh(auto_obj)
    return auto_obj


def eliminar_auto(db: Session, auto_id: int):
    """
    Eliminación física (se mantiene para compatibilidad).
    Evítala si quieres conservar el historial de ventas.
    """
    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
    return auto


def obtener_autos_vendidos(db: Session):
    """
    Devuelve todos los autos que ya fueron vendidos (vendido=True).
    """
    return db.query(Auto).filter(Auto.vendido == True).all()
