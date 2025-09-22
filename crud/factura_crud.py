"""
Funciones CRUD para la entidad Factura.

Este módulo permite crear, consultar y eliminar facturas en la base de datos.
"""

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
    :type db: sqlalchemy.orm.Session
    :param factura: Datos para la creación de la factura.
    :type factura: schemas.factura_schema.FacturaCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Factura recién creado.
    :rtype: database.entities.factura.Factura
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
    Obtiene todas las facturas registradas en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos Factura.
    :rtype: list[database.entities.factura.Factura]
    """

    return db.query(Factura).all()


def eliminar_factura(db: Session, factura_id: UUID):
    """
    Elimina una factura de la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param factura_id: ID de la factura a eliminar.
    :type factura_id: uuid.UUID
    :return: Objeto Factura eliminado si existía, de lo contrario None.
    :rtype: database.entities.factura.Factura | None
    """
    
    factura = db.query(Factura).filter(Factura.id == factura_id).first()
    if factura:
        db.delete(factura)
        db.commit()
    return factura
