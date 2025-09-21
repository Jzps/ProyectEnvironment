"""
Módulo de acceso y definición de la base de datos.

Este paquete centraliza la configuración de la conexión,
la inicialización de las tablas y la definición de los
modelos ORM utilizados en la aplicación.

Componentes principales
-----------------------
engine : sqlalchemy.Engine
    Motor de conexión a la base de datos, configurado según `config.py`.

SessionLocal : sqlalchemy.orm.sessionmaker
    Fábrica de sesiones para interactuar con la base de datos.

init_db() : Callable
    Función para inicializar la base de datos creando las tablas
    definidas en los modelos.

Modelos ORM
-----------
Auto :
    Representa los automóviles disponibles en el sistema.

Cliente :
    Información de los clientes (datos personales y de contacto).

Concesionario :
    Datos de los concesionarios donde trabajan los empleados.

Empleado :
    Datos generales de los empleados (vendedores o técnicos).

EmpleadoVendedor :
    Relación que identifica a un empleado como vendedor.

EmpleadoMantenimiento :
    Relación que identifica a un empleado como técnico de mantenimiento.

Especialidad :
    Tipos de especialidad de los técnicos.

empleado_mantenimiento_especialidad :
    Tabla intermedia para la relación muchos-a-muchos
    entre técnicos de mantenimiento y sus especialidades.

Mantenimiento :
    Registro de mantenimientos realizados a los automóviles.

Factura :
    Registro de facturación de ventas y mantenimientos.

Admin :
    Datos de los usuarios administradores del sistema.
"""

from .config import engine, SessionLocal
from .init_db import init_db
from .entities.auto import Auto
from .entities.cliente import Cliente
from .entities.concesionario import Concesionario
from .entities.empleado import Empleado
from .entities.empleado_vendedor import EmpleadoVendedor
from .entities.empleado_mantenimiento import EmpleadoMantenimiento
from .entities.especialidad import Especialidad, empleado_mantenimiento_especialidad
from .entities.mantenimiento import Mantenimiento
from .entities.factura import Factura
from .entities.admin import Admin

__all__ = [
    "engine",
    "SessionLocal",
    "init_db",
    "Auto",
    "Cliente",
    "Concesionario",
    "Empleado",
    "EmpleadoVendedor",
    "EmpleadoMantenimiento",
    "Especialidad",
    "empleado_mantenimiento_especialidad",
    "Mantenimiento",
    "Factura",
    "Admin",
]
