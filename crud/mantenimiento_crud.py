from sqlalchemy.orm import Session
from database.entities.mantenimiento import Mantenimiento
from schemas.mantenimiento_schema import MantenimientoCreate


def obtener_mantenimientos_por_auto(db: Session, auto_id: int):
    """Devuelve los mantenimientos asociados a un auto específico"""
    return db.query(Mantenimiento).filter(Mantenimiento.auto_id == auto_id).all()


def registrar_mantenimiento(db: Session, mantenimiento: MantenimientoCreate):
    db_mant = Mantenimiento(
        auto_id=mantenimiento.auto_id,
        empleado_id=mantenimiento.empleado_id,
        fecha=mantenimiento.fecha,
        detalle=mantenimiento.detalle,
        costo=mantenimiento.costo,
        factura_id=mantenimiento.factura_id,
    )
    db.add(db_mant)
    db.commit()
    db.refresh(db_mant)
    return db_mant


def obtener_mantenimientos(db: Session):
    """Devuelve la lista de mantenimientos registrados en la BD"""
    return db.query(Mantenimiento).all()
