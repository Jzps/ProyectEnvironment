from sqlalchemy.orm import Session
from database.entities.empleado import Empleado
from database.entities.empleado_vendedor import EmpleadoVendedor
from database.entities.empleado_mantenimiento import EmpleadoMantenimiento
from schemas.empleado_schema import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate

def crear_empleado(db: Session, empleado: EmpleadoCreate):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def obtener_empleados(db: Session):
    return db.query(Empleado).all()

def registrar_vendedor(db: Session, vendedor: VendedorCreate):
    db_vendedor = EmpleadoVendedor(**vendedor.dict())
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor

def obtener_vendedores(db: Session):
    return db.query(EmpleadoVendedor).all()

def registrar_mantenimiento_empleado(db: Session, tecnico: MantenimientoEmpleadoCreate):
    db_tecnico = EmpleadoMantenimiento(**tecnico.dict())
    db.add(db_tecnico)
    db.commit()
    db.refresh(db_tecnico)
    return db_tecnico

def obtener_tecnicos(db: Session):
    return db.query(EmpleadoMantenimiento).all()