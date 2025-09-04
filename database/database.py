from database.config import Base, engine
from database.entities import auto

def init_db():
    Base.metadata.create_all(bind=engine)
