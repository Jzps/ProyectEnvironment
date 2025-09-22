"""
Configuración de la conexión a la base de datos.

Este módulo carga las variables de entorno, valida la URL de
conexión y prepara los objetos necesarios para trabajar con
SQLAlchemy en la aplicación.

Variables y Objetos
-------------------
DATABASE_URL : str
    Cadena de conexión a la base de datos, obtenida del archivo .env.

engine : sqlalchemy.engine.Engine
    Motor de conexión a la base de datos creado a partir de DATABASE_URL.

SessionLocal : sqlalchemy.orm.sessionmaker
    Fábrica de sesiones para interactuar con la base de datos.
    Cada sesión debe abrirse y cerrarse de manera controlada
    (por ejemplo, dentro de un contexto o try/finally).

Excepciones
-----------
ValueError
    Se lanza si la variable de entorno `DATABASE_URL` no está definida.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from .base import Base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definida. Verifica tu archivo .env")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
