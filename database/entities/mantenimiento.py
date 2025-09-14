from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database.config import Base

class Mantenimiento(Base):
    __tablename__ = "mantenimientos"

    id = Column(Integer, primary_key=True, index=True)
    auto_id = Column(Integer, ForeignKey("autos.id"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados_mantenimiento.empleado_id"), nullable=False)
    fecha = Column(Date, nullable=False)
    detalle = Column(String, nullable=False)
    costo = Column(Float, nullable=False)
    factura_id = Column(Integer, ForeignKey("facturas.id"), nullable=True)