from .auto_crud import crear_auto, obtener_autos, eliminar_auto
from .cliente_crud import crear_cliente, obtener_clientes, obtener_cliente, eliminar_cliente
from .concesionario_crud import crear_concesionario, obtener_concesionarios
from .empleado_crud import (
    crear_empleado, obtener_empleados,
    registrar_vendedor, obtener_vendedores,
    registrar_mantenimiento_empleado, obtener_tecnicos
)
from .especialidad_crud import crear_especialidad, obtener_especialidades
from .mantenimiento_crud import registrar_mantenimiento, obtener_mantenimientos
from .factura_crud import crear_factura, obtener_facturas

__all__ = [
    "crear_auto", "obtener_autos", "eliminar_auto",
    "crear_cliente", "obtener_clientes", "obtener_cliente", "eliminar_cliente",
    "crear_concesionario", "obtener_concesionarios",
    "crear_empleado", "obtener_empleados",
    "registrar_vendedor", "obtener_vendedores",
    "registrar_mantenimiento_empleado", "obtener_tecnicos",
    "crear_especialidad", "obtener_especialidades",
    "registrar_mantenimiento", "obtener_mantenimientos",
    "crear_factura", "obtener_facturas",
]