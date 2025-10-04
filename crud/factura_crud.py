import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.factura import Factura
from schemas.factura_schema import FacturaCreate
from uuid import UUID


def crear_factura(db: Session, factura: FacturaCreate, usuario_id: UUID | None = None):
    """
    Crea una nueva factura en la base de datos.
    :param db: Sesión activa de SQLAlchemy.
    :param factura: Datos de la factura a crear.
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :return: Objeto Factura recién creado.
    """
    db_factura = Factura(
        id=uuid.uuid4(),
        **factura.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura


def obtener_facturas(db: Session):
    """
    Retorna todas las facturas registradas.
    :param db: Sesión activa de SQLAlchemy.
    :return: Lista de objetos Factura.
    """
    return db.query(Factura).all()


def eliminar_factura(db: Session, factura_id: UUID):
    """
    Elimina una factura por su ID.
    :param db: Sesión activa de SQLAlchemy.
    :param factura_id: ID de la factura a eliminar.
    :return: Factura eliminada o None si no existía.
    """
    factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if factura:
        db.delete(factura)
        db.commit()
    return factura


def eliminar_factura(db: Session, factura_id: UUID):
    factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if factura:
        db.delete(factura)
        db.commit()
    return factura
