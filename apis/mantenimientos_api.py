from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from crud import mantenimiento_crud
from schemas.mantenimiento_schema import MantenimientoCreate, MantenimientoOut
from typing import List
from uuid import UUID

router = APIRouter(
    prefix="/mantenimientos",
    tags=["Mantenimientos"],
    responses={404: {"description": "No encontrado"}},
)


@router.post("/", response_model=MantenimientoOut, status_code=201)
def crear_mantenimiento(
    mantenimiento: MantenimientoCreate, db: Session = Depends(get_db)
):
    """
    Registra un nuevo mantenimiento en el sistema y genera su factura automáticamente.
    """
    nuevo_mantenimiento = mantenimiento_crud.crear_mantenimiento(db, mantenimiento)

    if not nuevo_mantenimiento:
        raise HTTPException(
            status_code=400, detail="No se pudo registrar el mantenimiento"
        )

    return nuevo_mantenimiento


@router.get("/", response_model=List[MantenimientoOut])
def listar_mantenimientos(db: Session = Depends(get_db)):
    """
    Lista todos los mantenimientos registrados.
    Retorna una lista con los detalles de cada mantenimiento.
    """
    return mantenimiento_crud.obtener_mantenimientos(db)


@router.get("/{mantenimiento_id}", response_model=MantenimientoOut)
def obtener_mantenimiento(mantenimiento_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene un mantenimiento específico por ID.
    Retorna el mantenimiento si existe, o error 404.
    """
    mantenimiento = mantenimiento_crud.obtener_mantenimiento_por_id(
        db, mantenimiento_id
    )
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return mantenimiento


@router.delete("/{mantenimiento_id}")
def eliminar_mantenimiento(mantenimiento_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un mantenimiento existente por ID.
    Retorna confirmación o error 404 si no existe.
    """
    mantenimiento = mantenimiento_crud.eliminar_mantenimiento(db, mantenimiento_id)
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return {"mensaje": "Mantenimiento eliminado correctamente"}
