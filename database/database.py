from database.config import Base, engine

from database.entities import (
    auto,              
    cliente,
    concesionario,
    empleado,
    empleado_vendedor,
    empleado_mantenimiento,
    especialidad,
    mantenimiento,
    factura,
)

def init_db():
    Base.metadata.create_all(bind=engine)