from sqlalchemy.orm import Session
from database.entities.cliente import Cliente
from schemas.cliente_schema import ClienteCreate

def crear_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def obtener_clientes(db: Session):
    return db.query(Cliente).all()

def obtener_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.id == cliente_id).first()

def eliminar_cliente(db: Session, cliente_id: int):
    cliente = obtener_cliente(db, cliente_id)
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente