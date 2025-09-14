from sqlalchemy import Column, Integer, ForeignKey
from database.config import Base

class EmpleadoVendedor(Base):
    __tablename__ = "empleados_vendedor"

    empleado_id = Column(Integer, ForeignKey("empleados.id"), primary_key=True)