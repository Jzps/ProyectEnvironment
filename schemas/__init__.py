from .cliente_schema import ClienteCreate, ClienteOut
from .empleado_schema import (
    EmpleadoCreate,
    EmpleadoOut,
    VendedorCreate,
    VendedorOut,
    MantenimientoEmpleadoCreate,
    MantenimientoEmpleadoOut,
)
from .mantenimiento_schema import MantenimientoCreate, MantenimientoOut
from .factura_schema import FacturaCreate, FacturaOut
from .concesionario_schema import ConcesionarioCreate, ConcesionarioOut
from .auto_schema import AutoBase, AutoCreate, AutoOut
from .admin_schema import AdminCreate, AdminOut
from .especialidad_schema import EspecialidadCreate, EspecialidadOut

__all__ = [
    "ClienteCreate",
    "ClienteOut",
    "EmpleadoCreate",
    "EmpleadoOut",
    "VendedorCreate",
    "VendedorOut",
    "MantenimientoEmpleadoCreate",
    "MantenimientoEmpleadoOut",
    "MantenimientoCreate",
    "MantenimientoOut",
    "FacturaCreate",
    "FacturaOut",
    "ConcesionarioCreate",
    "ConcesionarioOut",
    "AutoBase",
    "AutoCreate",
    "AutoOut",
    "AdminCreate",
    "AdminOut",
    "EspecialidadCreate",
    "EspecialidadOut",
]
