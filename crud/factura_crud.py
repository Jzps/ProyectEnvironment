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
    """
    Devuelve todas las facturas registradas en la base de datos.
    """
    return db.query(Factura).all()


def eliminar_factura(db: Session, factura_id: int):
    """
    Elimina una factura por su ID si existe.
    """
    factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if factura:
        db.delete(factura)
        db.commit()
    return factura
