from database.config import engine
from database.base import Base
from database.entities import *


def init_db():
    Base.metadata.create_all(bind=engine)
