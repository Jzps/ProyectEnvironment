"""
Inicializa la base de datos de la aplicación.

Este módulo crea todas las tablas definidas en los modelos
de SQLAlchemy que heredan de `Base`.
"""

from database.config import engine
from database.base import Base
from database.entities import *


def init_db():
    """
    Crea en la base de datos todas las tablas definidas en los
    modelos de la aplicación.

    - Usa el `engine` configurado en `database.config`.
    - Si las tablas ya existen, no las modifica (operación idempotente).
    """
    Base.metadata.create_all(bind=engine)
