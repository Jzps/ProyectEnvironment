"""
Definición de la base declarativa y mixin de auditoría para el ORM.

Este módulo centraliza la configuración básica de SQLAlchemy
y provee un mixin reutilizable para añadir campos de auditoría
en las entidades de la base de datos.

Clases
------
Base : sqlalchemy.orm.declarative_base
    Clase base declarativa de SQLAlchemy que deben heredar
    todos los modelos de la aplicación.

AuditMixin :
    Mixin que agrega automáticamente a un modelo las columnas
    de auditoría más comunes:
        - id_usuario_creacion : UUID del usuario que creó el registro.
        - id_usuario_edicion  : UUID del último usuario que modificó el registro.
        - fecha_creacion      : Fecha y hora de creación del registro.
        - fecha_actualizacion : Fecha y hora de la última actualización.
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AuditMixin:
    """
    Mixin reutilizable para columnas de auditoría.
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
