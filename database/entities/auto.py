from sqlalchemy import Column, Integer, String, Float
from database.config import Base

class Auto(Base):
    __tablename__ = "autos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    precio = Column(Float)
    tipo = Column(String)  # Nuevo, Usado, Eléctrico
    extra = Column(String, nullable=True)  # Kilometraje o autonomía
