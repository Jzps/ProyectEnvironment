"""
Módulo de entidades del modelo de datos.

Este paquete centraliza la importación de todas las clases de entidades
(SQLAlchemy ORM) que representan las tablas principales de la base de datos 
del sistema de concesionarios. 

Clases y objetos exportados en ``__all__``:
- Admin: Representa un administrador del sistema.
- Auto: Representa un automóvil disponible o vendido.
- Cliente: Representa un cliente del concesionario.
- Concesionario: Representa un concesionario o sucursal.
- Empleado: Representa un empleado genérico.
- EmpleadoMantenimiento: Representa la relación de un empleado
  que realiza trabajos de mantenimiento.
- EmpleadoVendedor: Representa la relación de un empleado que actúa como vendedor.
- Especialidad: Representa una especialidad de mantenimiento técnico.
- Factura: Representa una factura de venta o de servicio.
- Mantenimiento: Representa un registro de mantenimiento de un vehículo.
- empleado_mantenimiento_especialidad: Tabla de asociación entre técnicos 
  de mantenimiento y sus especialidades.

Este módulo permite importar las entidades desde un solo lugar:
    from database.entities import Auto, Cliente, Factura, ...
"""

from .admin import Admin
from .auto import Auto
from .cliente import Cliente
from .concesionario import Concesionario
from .empleado import Empleado
from .empleado_vendedor import EmpleadoVendedor
from .empleado_mantenimiento import EmpleadoMantenimiento
from .especialidad import Especialidad, empleado_mantenimiento_especialidad
from .factura import Factura
from .mantenimiento import Mantenimiento

__all__ = [
    "Admin",
    "Auto",
    "Cliente",
    "Concesionario",
    "Empleado",
    "EmpleadoMantenimiento",
    "EmpleadoVendedor",
    "Especialidad",
    "Factura",
    "Mantenimiento",
    "empleado_mantenimiento_especialidad",
]
