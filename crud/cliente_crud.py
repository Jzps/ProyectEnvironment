import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.cliente import Cliente
from schemas.cliente_schema import ClienteCreate
from uuid import UUID


def crear_cliente(db: Session, cliente: ClienteCreate, usuario_id: UUID | None = None):
    """
    Crea un nuevo cliente con los datos proporcionados.
    :param db: Sesión activa de SQLAlchemy.
    :param cliente: Datos del cliente a crear.
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :return: Objeto Cliente recién creado.
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
    Retorna todos los clientes de la base de datos.
    :param db: Sesión activa de SQLAlchemy.
    :return: Lista de objetos Cliente.
    """
    return db.query(Cliente).all()


def obtener_cliente(db: Session, cliente_id: UUID):
    """
    Busca un cliente por su ID único.
    :param db: Sesión activa de SQLAlchemy.
    :param cliente_id: Identificador del cliente.
    :return: Objeto Cliente o None si no existe.
    """
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def eliminar_cliente(db: Session, cliente_id: UUID):
    """
    Elimina un cliente de la base de datos.
    :param db: Sesión activa de SQLAlchemy.
    :param cliente_id: ID del cliente a eliminar.
    :return: Cliente eliminado o None si no existía.
    """
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente


def actualizar_cliente(db: Session, cliente_id: UUID, cliente: ClienteCreate):
    db_cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
    if db_cliente:
        for key, value in cliente.dict().items():
            setattr(db_cliente, key, value)
        db.commit()
        db.refresh(db_cliente)
    return db_cliente
