"""
Funciones CRUD para la entidad Concesionario.

Este módulo contiene las operaciones básicas para crear y consultar
concesionarios en la base de datos.
"""

import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.concesionario import Concesionario
from schemas.concesionario_schema import ConcesionarioCreate
from uuid import UUID


def crear_concesionario(
    db: Session, concesionario: ConcesionarioCreate, usuario_id: UUID | None = None
):
    """
    Crea un nuevo concesionario en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param concesionario: Datos necesarios para crear el concesionario.
    :type concesionario: schemas.concesionario_schema.ConcesionarioCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Concesionario recién creado.
    :rtype: database.entities.concesionario.Concesionario
    """

    db_concesionario = Concesionario(
        id=uuid.uuid4(),
        **concesionario.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_concesionario)
    db.commit()
    db.refresh(db_concesionario)
    return db_concesionario


def obtener_concesionarios(db: Session):
    """
    Obtiene todos los concesionarios registrados en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos Concesionario.
    :rtype: list[database.entities.concesionario.Concesionario]
    """
    
    return db.query(Concesionario).all()
