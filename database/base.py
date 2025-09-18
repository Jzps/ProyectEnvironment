# database/base.py
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AuditMixin:
    """
    Mezcla reusables para columnas de auditoría.
    """

    id_usuario_creacion = Column(PG_UUID(as_uuid=True), nullable=True)
    id_usuario_edicion = Column(PG_UUID(as_uuid=True), nullable=True)
    fecha_creacion = Column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
    fecha_actualizacion = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True,
    )
