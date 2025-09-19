import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.cliente import Cliente
from schemas.cliente_schema import ClienteCreate
from uuid import UUID


def crear_cliente(db: Session, cliente: ClienteCreate, usuario_id: UUID | None = None):
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
    return db.query(Cliente).all()


def obtener_cliente(db: Session, cliente_id: UUID):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()


def eliminar_cliente(db: Session, cliente_id: UUID):
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente
