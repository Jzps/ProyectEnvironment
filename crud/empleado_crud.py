"""
Funciones CRUD para la entidad Empleado.

Este módulo incluye las operaciones para crear empleados,
registrar su rol como vendedor o técnico de mantenimiento,
y consultar las listas correspondientes.
"""

import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities.empleado import Empleado
from database.entities.empleado_vendedor import EmpleadoVendedor
from database.entities.empleado_mantenimiento import EmpleadoMantenimiento
from schemas.empleado_schema import (
    EmpleadoCreate,
    VendedorCreate,
    MantenimientoEmpleadoCreate,
)
from uuid import UUID


def crear_empleado(
    db: Session, empleado: EmpleadoCreate, usuario_id: UUID | None = None
):
    """
    Crea un nuevo empleado en la base de datos.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param empleado: Datos para la creación del empleado.
    :type empleado: schemas.empleado_schema.EmpleadoCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto Empleado recién creado.
    :rtype: database.entities.empleado.Empleado
    """

    db_empleado = Empleado(
        id=uuid.uuid4(),
        **empleado.dict(),
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado


def obtener_empleados(db: Session):
    """
    Obtiene todos los empleados registrados.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos Empleado.
    :rtype: list[database.entities.empleado.Empleado]
    """

    return db.query(Empleado).all()


def registrar_vendedor(
    db: Session, vendedor: VendedorCreate, usuario_id: UUID | None = None
):
    """
    Registra un empleado como vendedor.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param vendedor: Datos para asociar un empleado al rol de vendedor.
    :type vendedor: schemas.empleado_schema.VendedorCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto EmpleadoVendedor recién creado.
    :rtype: database.entities.empleado_vendedor.EmpleadoVendedor
    """

    db_vendedor = EmpleadoVendedor(
        empleado_id=vendedor.empleado_id,
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor


def obtener_vendedores(db: Session):
    """
    Obtiene todos los empleados registrados como vendedores.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos EmpleadoVendedor.
    :rtype: list[database.entities.empleado_vendedor.EmpleadoVendedor]
    """

    return db.query(EmpleadoVendedor).all()


def registrar_mantenimiento_empleado(
    db: Session, tecnico: MantenimientoEmpleadoCreate, usuario_id: UUID | None = None
):
    """
    Registra un empleado como técnico de mantenimiento.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :param tecnico: Datos para asociar un empleado como técnico.
    :type tecnico: schemas.empleado_schema.MantenimientoEmpleadoCreate
    :param usuario_id: ID del usuario que crea el registro (opcional).
    :type usuario_id: uuid.UUID | None
    :return: Objeto EmpleadoMantenimiento recién creado.
    :rtype: database.entities.empleado_mantenimiento.EmpleadoMantenimiento
    """

    db_tecnico = EmpleadoMantenimiento(
        empleado_id=tecnico.empleado_id,
        tipo_carro=tecnico.tipo_carro,
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_tecnico)
    db.commit()
    db.refresh(db_tecnico)
    return db_tecnico


def obtener_tecnicos(db: Session):
    """
    Obtiene todos los empleados registrados como técnicos de mantenimiento.

    :param db: Sesión activa de SQLAlchemy.
    :type db: sqlalchemy.orm.Session
    :return: Lista de objetos EmpleadoMantenimiento.
    :rtype: list[database.entities.empleado_mantenimiento.EmpleadoMantenimiento]
    """
    
    return db.query(EmpleadoMantenimiento).all()
