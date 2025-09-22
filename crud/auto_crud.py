"""
Funciones CRUD para la entidad Auto.

Este módulo define las operaciones de creación, consulta,
actualización y eliminación de registros de automóviles en la base de datos.
"""

import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate
from uuid import UUID


def crear_auto(db: Session, auto: AutoCreate, usuario_id: UUID | None = None):
    """
    Crea un nuevo automóvil en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param auto: Datos para la creación del automóvil (marca, modelo, precio, tipo, extra).
    :type auto: schemas.auto_schema.AutoCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Auto recién creado.
    :rtype: database.entities.auto.Auto
    """

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
    """
    Obtiene la lista de automóviles.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param disponibles_only: Si es True, filtra solo los autos no vendidos.
    :type disponibles_only: bool
    :return: Lista de objetos Auto según el filtro.
    :rtype: list[database.entities.auto.Auto]
    """

    q = db.query(Auto)
    if disponibles_only:
        q = q.filter(Auto.vendido == False)
    return q.all()


def obtener_auto_por_id(db: Session, auto_id: UUID):
    return db.query(Auto).filter(Auto.id == auto_id).first()
"""
    Busca un automóvil por su identificador único.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param auto_id: ID del automóvil a consultar.
    :type auto_id: uuid.UUID
    :return: Objeto Auto si existe, de lo contrario None.
    :rtype: database.entities.auto.Auto | None
    """

def marcar_vendido(db: Session, auto_id: UUID, usuario_id: UUID | None = None):
    """
    Marca un automóvil como vendido y actualiza la información de edición.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param auto_id: ID del automóvil a marcar como vendido.
    :type auto_id: uuid.UUID
    :param usuario_id: ID del usuario que realiza la modificación (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Auto actualizado, o None si no existe.
    :rtype: database.entities.auto.Auto | None
    """
     
    auto_obj = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto_obj:
        auto_obj.vendido = True
        auto_obj.id_usuario_edicion = usuario_id
        auto_obj.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(auto_obj)
    return auto_obj


def eliminar_auto(db: Session, auto_id: UUID):
    """
    Elimina un automóvil de la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param auto_id: ID del automóvil a eliminar.
    :type auto_id: uuid.UUID
    :return: Objeto Auto eliminado si existía, de lo contrario None.
    :rtype: database.entities.auto.Auto | None
    """

    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
    return auto


def obtener_autos_vendidos(db: Session):
    return db.query(Auto).filter(Auto.vendido == True).all()
"""
    Obtiene la lista de automóviles que ya han sido vendidos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de autos vendidos.
    :rtype: list[database.entities.auto.Auto]
    """
