from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database.config import Base

class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    dni = Column(String, unique=True)
    correo = Column(String)
    telefono = Column(String)
    fecha_contratacion = Column(Date)
    concesionario_id = Column(Integer, ForeignKey("concesionarios.id"), nullable=True)