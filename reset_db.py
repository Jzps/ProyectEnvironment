from database.config import engine
from database.base import Base
from database.entities import *


def reset_db():

    print("Eliminando todas las tablas existentes...")
    Base.metadata.drop_all(bind=engine)
    print("Tablas eliminadas")

    print("Creando tablas según los modelos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas")


if __name__ == "__main__":
    reset_db()
