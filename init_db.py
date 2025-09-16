from database.config import engine
from database.base import Base
import database.entities

Base.metadata.create_all(bind=engine)
print("[SUCCESS] Todas las tablas han sido creadas")
