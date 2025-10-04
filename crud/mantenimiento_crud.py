import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.mantenimiento import Mantenimiento
from schemas.mantenimiento_schema import MantenimientoCreate
from uuid import UUID


def crear_mantenimiento(
    db: Session, mantenimiento: MantenimientoCreate, usuario_id=None
):
    """
    Crea un mantenimiento en la base de datos. No genera ni refiere facturas.
    """
    db_mantenimiento = Mantenimiento(
        id=uuid.uuid4(),
        auto_id=mantenimiento.auto_id,
        empleado_id=mantenimiento.empleado_id,
        cliente_id=mantenimiento.cliente_id,
        fecha=mantenimiento.fecha,
        detalle=mantenimiento.detalle,
        costo=mantenimiento.costo,
        id_usuario_creacion=usuario_id,
    )
    db.add(db_mantenimiento)
    db.commit()
    db.refresh(db_mantenimiento)
    return db_mantenimiento


def obtener_mantenimientos_por_auto(db: Session, auto_id: UUID):
    """
    Retorna todos los mantenimientos de un vehículo específico.
    """
    return db.query(Mantenimiento).filter(Mantenimiento.auto_id == auto_id).all()


def registrar_mantenimiento(
    db: Session, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
):
    """
    Alias para crear_mantenimiento (mantener compatibilidad).
    """
    return crear_mantenimiento(db, mantenimiento, usuario_id)


def obtener_mantenimientos(db: Session):
    """
    Retorna todos los mantenimientos registrados.
    """
    return db.query(Mantenimiento).all()


def obtener_mantenimiento_por_id(db: Session, mantenimiento_id: UUID):
    """
    Retorna un mantenimiento por su ID o None si no existe.
    """
    return db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()


def eliminar_mantenimiento(db: Session, mantenimiento_id: UUID):
    mantenimiento = (
        db.query(Mantenimiento).filter(Mantenimiento.id == mantenimiento_id).first()
    )
    if mantenimiento:
        db.delete(mantenimiento)
        db.commit()
    return mantenimiento
