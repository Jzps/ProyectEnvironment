from sqlalchemy.orm import Session
from database.entities.factura import Factura
from schemas.factura_schema import FacturaCreate

def crear_factura(db: Session, factura: FacturaCreate):
    db_factura = Factura(**factura.dict())
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura

def obtener_facturas(db: Session):
    return db.query(Factura).all()