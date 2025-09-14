from .cliente_crud import (
    crear_cliente,
    obtener_clientes,
    obtener_cliente,
    eliminar_cliente,
)
from .empleado_crud import (
    crear_empleado,
    obtener_empleados,
    registrar_vendedor,
    obtener_vendedores,
    registrar_mantenimiento_empleado,
    obtener_tecnicos,
)
from .mantenimiento_crud import (
    registrar_mantenimiento,
    obtener_mantenimientos,
    obtener_mantenimientos_por_auto,
)
from .factura_crud import (
    crear_factura,
    obtener_facturas,
    eliminar_factura,
)
from .auto_crud import (
    crear_auto,
    obtener_autos,
    obtener_auto_por_id,
    marcar_vendido,
    eliminar_auto,
    obtener_autos_vendidos,
)
from .concesionario_crud import (
    crear_concesionario,
    obtener_concesionarios,
)
from .admin_crud import (
    crear_admin,
    obtener_admin,
)

__all__ = [
    "crear_cliente",
    "obtener_clientes",
    "obtener_cliente",
    "eliminar_cliente",
    "crear_empleado",
    "obtener_empleados",
    "registrar_vendedor",
    "obtener_vendedores",
    "registrar_mantenimiento_empleado",
    "obtener_tecnicos",
    "registrar_mantenimiento",
    "obtener_mantenimientos",
    "obtener_mantenimientos_por_auto",
    "crear_factura",
    "obtener_facturas",
    "eliminar_factura",
    "crear_auto",
    "obtener_autos",
    "obtener_auto_por_id",
    "marcar_vendido",
    "eliminar_auto",
    "obtener_autos_vendidos",
    "crear_concesionario",
    "obtener_concesionarios",
    "crear_admin",
    "obtener_admin",
]
