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
    return db.query(Empleado).all()


def registrar_vendedor(
    db: Session, vendedor: VendedorCreate, usuario_id: UUID | None = None
):
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
    return db.query(EmpleadoVendedor).all()


def registrar_mantenimiento_empleado(
    db: Session, tecnico: MantenimientoEmpleadoCreate, usuario_id: UUID | None = None
):
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
    return db.query(EmpleadoMantenimiento).all()
