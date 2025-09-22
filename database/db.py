"""
Inicialización de la base de datos.

Este módulo expone una función utilitaria para crear todas
las tablas definidas en los modelos ORM de la aplicación.
Se apoya en el motor de conexión configurado en `database.config`.
"""

from database.config import engine
from database.base import Base
from database.entities import *


def init_db():
    """
    Crea en la base de datos todas las tablas definidas en los
    modelos ORM registrados en `Base.metadata`.

    Usa el motor de conexión (`engine`) configurado en el módulo
    `database.config`.

    Esta función es idempotente: si las tablas ya existen,
    no se volverán a crear ni se alterarán.
    """
    
    Base.metadata.create_all(bind=engine)
