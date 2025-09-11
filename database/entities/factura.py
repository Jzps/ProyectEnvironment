from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, UniqueConstraint
from database.config import Base

class Factura(Base):
    __tablename__ = "facturas"
    __table_args__ = (
        UniqueConstraint("auto_id", name="uix_factura_auto_unico"),
    )

    id = Column(Integer, primary_key=True, index=True)
    fecha_emision = Column(Date, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    empleado_id = Column(Integer, ForeignKey("empleados_vendedor.empleado_id"), nullable=False)
    auto_id = Column(Integer, ForeignKey("autos.id"), nullable=False)
    precio_carro_base = Column(Float, nullable=False)
    costo_mantenimiento = Column(Float, nullable=False, default=0.0)
    descuento = Column(Float, nullable=False, default=0.0)
    total = Column(Float, nullable=False)
    observaciones = Column(String, nullable=True)