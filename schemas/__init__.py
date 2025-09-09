from .auto_schema import AutoBase, AutoCreate, AutoOut
from .cliente_schema import ClienteBase, ClienteCreate, ClienteOut
from .concesionario_schema import ConcesionarioBase, ConcesionarioCreate, ConcesionarioOut
from .empleado_schema import (
    EmpleadoBase, EmpleadoCreate, EmpleadoOut,
    VendedorCreate, VendedorOut,
    MantenimientoEmpleadoCreate, MantenimientoEmpleadoOut
)
from .especialidad_schema import EspecialidadBase, EspecialidadCreate, EspecialidadOut
from .mantenimiento_schema import MantenimientoBase, MantenimientoCreate, MantenimientoOut
from .factura_schema import FacturaBase, FacturaCreate, FacturaOut

__all__ = [
    "AutoBase", "AutoCreate", "AutoOut",
    "ClienteBase", "ClienteCreate", "ClienteOut",
    "ConcesionarioBase", "ConcesionarioCreate", "ConcesionarioOut",
    "EmpleadoBase", "EmpleadoCreate", "EmpleadoOut",
    "VendedorCreate", "VendedorOut",
    "MantenimientoEmpleadoCreate", "MantenimientoEmpleadoOut",
    "EspecialidadBase", "EspecialidadCreate", "EspecialidadOut",
    "MantenimientoBase", "MantenimientoCreate", "MantenimientoOut",
    "FacturaBase", "FacturaCreate", "FacturaOut",
]
