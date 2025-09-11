from sqlalchemy import Column, Integer, String, Table, ForeignKey
from database.config import Base

empleado_mantenimiento_especialidad = Table(
    "empleado_mantenimiento_especialidad",
    Base.metadata,
    Column("empleado_id", Integer, ForeignKey("empleados_mantenimiento.empleado_id"), primary_key=True),
    Column("especialidad_id", Integer, ForeignKey("especialidades.id"), primary_key=True),
)

class Especialidad(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)