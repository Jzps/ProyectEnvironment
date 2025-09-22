import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.auto import Auto
from schemas.auto_schema import AutoCreate
from uuid import UUID


def crear_auto(db: Session, auto: AutoCreate, usuario_id: UUID | None = None):
    """
    Crea un nuevo automóvil en la base de datos con los datos proporcionados.
    :param db: Sesión activa de SQLAlchemy.
    :param auto: Datos del automóvil a crear.
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :return: Objeto Auto recién creado.
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
    Retorna la lista de automóviles, filtrando opcionalmente por disponibles.
    :param db: Sesión activa de SQLAlchemy.
    :param disponibles_only: Filtra solo autos no vendidos si es True.
    :return: Lista de objetos Auto.
    """
    q = db.query(Auto)
    if disponibles_only:
        q = q.filter(Auto.vendido == False)
    return q.all()


def obtener_auto_por_id(db: Session, auto_id: UUID):
    """
    Busca un automóvil por su ID único.
    :param db: Sesión activa de SQLAlchemy.
    :param auto_id: Identificador del automóvil.
    :return: Objeto Auto o None si no existe.
    """
    return db.query(Auto).filter(Auto.id == auto_id).first()


def marcar_vendido(db: Session, auto_id: UUID, usuario_id: UUID | None = None):
    """
    Marca un automóvil como vendido y actualiza su información de edición.
    :param db: Sesión activa de SQLAlchemy.
    :param auto_id: ID del automóvil a actualizar.
    :param usuario_id: ID del usuario que realiza la modificación (opcional).
    :return: Auto actualizado o None si no existe.
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
    :param auto_id: ID del automóvil a eliminar.
    :return: Objeto Auto eliminado o None si no existía.
    """
    auto = db.query(Auto).filter(Auto.id == auto_id).first()
    if auto:
        db.delete(auto)
        db.commit()
    return auto


def obtener_autos_vendidos(db: Session):
    """
    Retorna la lista de automóviles que ya han sido vendidos.
    :param db: Sesión activa de SQLAlchemy.
    :return: Lista de autos vendidos.
    """
    return db.query(Auto).filter(Auto.vendido == True).all()
