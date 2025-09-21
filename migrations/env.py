"""
Archivo de configuración de Alembic para migraciones de la base de datos.

Este archivo se encarga de:
1. Cargar variables de entorno desde un archivo `.env` (como DATABASE_URL).
2. Configurar Alembic para ejecutar migraciones en modo offline o online.
3. Registrar el metadata de SQLAlchemy para que Alembic pueda generar
   y aplicar cambios en la base de datos.
4. Importar todas las entidades de la base de datos necesarias para
   reflejar el esquema actual.

Funciones principales:
- run_migrations_offline(): Ejecuta migraciones sin conexión a la base de datos.
  Genera SQL en bruto que puede ejecutarse manualmente.
- run_migrations_online(): Ejecuta migraciones conectándose directamente
  a la base de datos.

El archivo utiliza:
- SQLAlchemy para la gestión del motor y las conexiones.
- Alembic para la gestión de migraciones.
- python-dotenv para cargar la configuración sensible.
"""

from dotenv import load_dotenv
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context


load_dotenv()


config = context.config

database_url = os.getenv("DATABASE_URL")

if database_url:
    config.set_main_option("sqlalchemy.url", database_url)


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


from database.config import Base


import database.entities.admin
import database.entities.auto
import database.entities.cliente
import database.entities.concesionario
import database.entities.empleado
import database.entities.empleado_mantenimiento
import database.entities.empleado_vendedor
import database.entities.especialidad
import database.entities.factura
import database.entities.mantenimiento

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones en modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
