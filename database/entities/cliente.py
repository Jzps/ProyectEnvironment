from sqlalchemy import Column, Integer, String
from database.base import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, unique=True)
    correo = Column(String)
    telefono = Column(String)
    direccion = Column(String)
