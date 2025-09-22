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
    """
    Ejecuta migraciones en modo offline.
    Genera el SQL sin conectarse a la base de datos.
    """
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
    """
    Ejecuta migraciones en modo online.
    Se conecta a la base de datos y aplica cambios directamente.
    """
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
