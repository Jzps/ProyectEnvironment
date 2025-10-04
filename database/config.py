# database/config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("No se encontró DATABASE_URL en el archivo .env")

# pool_pre_ping=True evita errores por conexiones cerradas en el pool
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependency de FastAPI para obtener y cerrar la sesión de BD.
    Se usa con Depends(get_db) en los endpoints.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
