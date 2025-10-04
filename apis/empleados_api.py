from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.empleado_schema import (
    EmpleadoCreate,
    VendedorCreate,
    MantenimientoEmpleadoCreate,
    EmpleadoOut,
)
from services.empleado_service import EmpleadoService
from crud import empleado_crud
from uuid import UUID
from typing import List

router = APIRouter(
    prefix="/empleados",
    tags=["Empleados"],
    responses={404: {"description": "No encontrado"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmpleadoOut, status_code=status.HTTP_201_CREATED)
def crear_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo empleado en el sistema.
    Retorna los datos del empleado registrado.
    """
    service = EmpleadoService(db)
    return service.registrar_empleado(empleado)


@router.get("/", response_model=List[EmpleadoOut])
def listar_empleados(db: Session = Depends(get_db)):
    """
    Lista todos los empleados registrados.
    Retorna una lista de objetos empleados.
    """
    service = EmpleadoService(db)
    return service.listar_empleados()


@router.get("/{empleado_id}", response_model=EmpleadoOut)
def obtener_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene la información de un empleado por su ID único.
    Lanza error 404 si no existe.
    """
    empleado = db.query(empleado_crud.Empleado).filter_by(id=empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.post("/vendedores")
def registrar_vendedor(vendedor: VendedorCreate, db: Session = Depends(get_db)):
    """
    Marca un empleado como vendedor.
    Requiere el ID del empleado existente.
    """
    service = EmpleadoService(db)
    return service.registrar_vendedor(vendedor)


@router.post("/tecnicos")
def registrar_tecnico(
    tecnico: MantenimientoEmpleadoCreate, db: Session = Depends(get_db)
):
    """
    Registra a un empleado como técnico de mantenimiento.
    Incluye el tipo de vehículos en los que se especializa.
    """
    service = EmpleadoService(db)
    return service.registrar_tecnico(tecnico)


@router.get("/vendedores")
def listar_vendedores(db: Session = Depends(get_db)):
    """
    Obtiene todos los empleados registrados como vendedores.
    Retorna la lista de vendedores actuales.
    """
    service = EmpleadoService(db)
    return service.listar_vendedores()


@router.get("/tecnicos")
def listar_tecnicos(db: Session = Depends(get_db)):
    """
    Obtiene todos los empleados registrados como técnicos.
    Retorna la lista de técnicos actuales.
    """
    service = EmpleadoService(db)
    return service.listar_tecnicos()


@router.put("/{empleado_id}", response_model=EmpleadoOut)
def actualizar_empleado(
    empleado_id: UUID, empleado: EmpleadoCreate, db: Session = Depends(get_db)
):
    """
    Actualiza los datos de un empleado existente.
    Retorna el empleado actualizado o error 404 si no existe.
    """
    db_empleado = empleado_crud.actualizar_empleado(db, empleado_id, empleado)
    if not db_empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado


@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un empleado de la base de datos.
    Retorna confirmación o error 404 si no existe.
    """
    empleado = empleado_crud.eliminar_empleado(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"mensaje": "Empleado eliminado correctamente"}
