from sqlalchemy import Column, Integer, String, ForeignKey
from database.config import Base


class EmpleadoMantenimiento(Base):
    __tablename__ = "empleados_mantenimiento"

    empleado_id = Column(Integer, ForeignKey("empleados.id"), primary_key=True)
    tipo_carro = Column(String, nullable=False)
