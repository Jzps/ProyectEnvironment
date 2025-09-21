"""
Paquete de exportación de esquemas Pydantic.

Este módulo centraliza y reexporta los modelos de datos (schemas) utilizados 
en la API para la validación de entradas y salidas. Permite importar de forma 
directa los esquemas principales desde `schemas` sin necesidad de referirse a 
cada archivo individual.

Contiene:
    ClienteCreate: Esquema para crear un nuevo cliente.
    EmpleadoCreate: Esquema para crear un empleado.
    VendedorCreate: Esquema para registrar un empleado como vendedor.
    MantenimientoEmpleadoCreate: Esquema para registrar un empleado de mantenimiento.
    MantenimientoCreate: Esquema para crear un registro de mantenimiento.
    FacturaCreate: Esquema para crear una factura de venta.
    ConcesionarioCreate: Esquema para crear un concesionario.
    AutoBase: Esquema base de autos (atributos comunes).
    AutoCreate: Esquema para crear un auto.
    AutoOut: Esquema para la salida (respuesta) de datos de un auto.
    AdminCreate: Esquema para crear un usuario administrador.
    AdminOut: Esquema para la salida (respuesta) de datos de un administrador.
"""

from .cliente_schema import ClienteCreate
from .empleado_schema import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate
from .mantenimiento_schema import MantenimientoCreate
from .factura_schema import FacturaCreate
from .concesionario_schema import ConcesionarioCreate
from .auto_schema import AutoBase, AutoCreate, AutoOut
from .admin_schema import AdminCreate, AdminOut

__all__ = [
    "ClienteCreate",
    "EmpleadoCreate",
    "VendedorCreate",
    "MantenimientoEmpleadoCreate",
    "MantenimientoCreate",
    "FacturaCreate",
    "ConcesionarioCreate",
    "AutoBase",
    "AutoCreate",
    "AutoOut",
    "AdminCreate",
    "AdminOut",
]
