from sqlalchemy import Column, Integer, String
from database.config import Base


class Concesionario(Base):
    __tablename__ = "concesionarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String)
    telefono = Column(String)
