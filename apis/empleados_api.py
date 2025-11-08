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
    service = EmpleadoService(db)
    return service.registrar_empleado(empleado)


@router.get("/", response_model=List[EmpleadoOut])
def listar_empleados(db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    return service.listar_empleados()


@router.get("/vendedores")
def listar_vendedores(db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    return service.listar_vendedores()


@router.get("/tecnicos")
def listar_tecnicos(db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    return service.listar_tecnicos()


@router.post("/vendedores")
def registrar_vendedor(vendedor: VendedorCreate, db: Session = Depends(get_db)):
    service = EmpleadoService(db)
    return service.registrar_vendedor(vendedor)


@router.post("/tecnicos")
def registrar_tecnico(
    tecnico: MantenimientoEmpleadoCreate, db: Session = Depends(get_db)
):
    service = EmpleadoService(db)
    return service.registrar_tecnico(tecnico)


@router.get("/{empleado_id}", response_model=EmpleadoOut)
def obtener_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    empleado = db.query(empleado_crud.Empleado).filter_by(id=empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado


@router.put("/{empleado_id}", response_model=EmpleadoOut)
def actualizar_empleado(
    empleado_id: UUID, empleado: EmpleadoCreate, db: Session = Depends(get_db)
):
    db_empleado = empleado_crud.actualizar_empleado(db, empleado_id, empleado)
    if not db_empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_empleado


@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    empleado = empleado_crud.eliminar_empleado(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"mensaje": "Empleado eliminado correctamente"}
