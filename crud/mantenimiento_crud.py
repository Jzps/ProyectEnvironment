import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.mantenimiento import Mantenimiento
from schemas.mantenimiento_schema import MantenimientoCreate
from uuid import UUID


def obtener_mantenimientos_por_auto(db: Session, auto_id: UUID):
    """
    Retorna todos los mantenimientos de un vehículo específico.
    :param db: Sesión activa de SQLAlchemy.
    :param auto_id: ID del auto a consultar.
    :return: Lista de objetos Mantenimiento.
    """
    return db.query(Mantenimiento).filter(Mantenimiento.auto_id == auto_id).all()


def registrar_mantenimiento(
    db: Session, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
):
    """
    Registra un nuevo mantenimiento en la base de datos.
    :param db: Sesión activa de SQLAlchemy.
    :param mantenimiento: Datos del mantenimiento a registrar.
    :param usuario_id: ID del usuario que realiza el registro (opcional).
    :return: Objeto Mantenimiento recién creado.
    """
    db_mant = Mantenimiento(
        id=uuid.uuid4(),
        auto_id=mantenimiento.auto_id,
        empleado_id=mantenimiento.empleado_id,
        fecha=mantenimiento.fecha,
        detalle=mantenimiento.detalle,
        costo=mantenimiento.costo,
        factura_id=mantenimiento.factura_id,
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_mant)
    db.commit()
    db.refresh(db_mant)
    return db_mant


def obtener_mantenimientos(db: Session):
    """
    Retorna todos los mantenimientos registrados.
    :param db: Sesión activa de SQLAlchemy.
    :return: Lista de objetos Mantenimiento.
    """
    return db.query(Mantenimiento).all()
