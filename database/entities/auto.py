from sqlalchemy import Boolean, Column, Float, Integer, String
from database.config import Base


class Auto(Base):
    __tablename__ = "autos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, index=True)
    precio = Column(Float)
    tipo = Column(String)
    extra = Column(String)
    vendido = Column(Boolean, default=False)
