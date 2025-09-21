"""
Funciones CRUD para la entidad Cliente.

Este módulo contiene las operaciones básicas para crear, consultar
y eliminar clientes en la base de datos.
"""

import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.cliente import Cliente
from schemas.cliente_schema import ClienteCreate
from uuid import UUID


def crear_cliente(db: Session, cliente: ClienteCreate, usuario_id: UUID | None = None):
    """
    Crea un nuevo cliente en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param cliente: Datos para la creación del cliente.
    :type cliente: schemas.cliente_schema.ClienteCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Cliente recién creado.
    :rtype: database.entities.cliente.Cliente
    """

    db_cliente = Cliente(
        id=uuid.uuid4(),
        **cliente.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def obtener_clientes(db: Session):
    """
    Obtiene todos los clientes de la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista con todos los objetos Cliente.
    :rtype: list[database.entities.cliente.Cliente]
    """

    return db.query(Cliente).all()


def obtener_cliente(db: Session, cliente_id: UUID):
    """
    Busca un cliente por su identificador único.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param cliente_id: ID del cliente a buscar.
    :type cliente_id: uuid.UUID
    :return: Objeto Cliente si existe, de lo contrario None.
    :rtype: database.entities.cliente.Cliente | None
    """

    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def eliminar_cliente(db: Session, cliente_id: UUID):
    """
    Elimina un cliente de la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param cliente_id: ID del cliente a eliminar.
    :type cliente_id: uuid.UUID
    :return: Objeto Cliente eliminado si existía, de lo contrario None.
    :rtype: database.entities.cliente.Cliente | None
    """
    
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente
