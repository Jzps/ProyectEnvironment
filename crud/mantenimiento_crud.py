"""
Funciones CRUD para la entidad Mantenimiento.

Permite registrar mantenimientos y consultar los existentes,
ya sea por vehículo específico o en general.
"""

import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.mantenimiento import Mantenimiento
from schemas.mantenimiento_schema import MantenimientoCreate
from uuid import UUID


def obtener_mantenimientos_por_auto(db: Session, auto_id: UUID):
    """
    Obtiene todos los mantenimientos asociados a un vehículo específico.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param auto_id: ID del auto del cual se desean los mantenimientos.
    :type auto_id: uuid.UUID
    :return: Lista de mantenimientos relacionados con el auto.
    :rtype: list[database.entities.mantenimiento.Mantenimiento]
    """
      
    return db.query(Mantenimiento).filter(Mantenimiento.auto_id == auto_id).all()


def registrar_mantenimiento(
    db: Session, mantenimiento: MantenimientoCreate, usuario_id: UUID | None = None
):
    """
    Registra un nuevo mantenimiento en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param mantenimiento: Datos necesarios para crear el mantenimiento.
    :type mantenimiento: schemas.mantenimiento_schema.MantenimientoCreate
    :param usuario_id: ID del usuario que realiza el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Mantenimiento recién creado.
    :rtype: database.entities.mantenimiento.Mantenimiento
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
    Obtiene todos los mantenimientos registrados en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de todos los mantenimientos.
    :rtype: list[database.entities.mantenimiento.Mantenimiento]
    """
    
    return db.query(Mantenimiento).all()
