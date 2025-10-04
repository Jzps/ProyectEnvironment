from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from crud import concesionario_crud
from schemas.concesionario_schema import ConcesionarioCreate, ConcesionarioOut
from database.entities.concesionario import Concesionario
from typing import List
from uuid import UUID

router = APIRouter(prefix="/concesionario", tags=["Concesionario"])


@router.post("/", response_model=ConcesionarioOut, status_code=201)
def crear_concesionario(
    concesionario: ConcesionarioCreate, db: Session = Depends(get_db)
):
    """
    Crea un nuevo concesionario en la base de datos.
    Devuelve el objeto recién registrado.
    """
    return concesionario_crud.crear_concesionario(db, concesionario)


@router.get("/", response_model=List[ConcesionarioOut])
def listar_concesionarios(db: Session = Depends(get_db)):
    """
    Lista todos los concesionarios disponibles.
    Retorna una lista de concesionarios.
    """
    return concesionario_crud.obtener_concesionarios(db)


@router.get("/{concesionario_id}", response_model=ConcesionarioOut)
def obtener_concesionario(concesionario_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene un concesionario por su ID único.
    Lanza error 404 si no existe.
    """
    concesionario = db.query(Concesionario).filter_by(id=concesionario_id).first()
    if not concesionario:
        raise HTTPException(status_code=404, detail="Concesionario no encontrado")
    return concesionario


@router.put("/{concesionario_id}", response_model=ConcesionarioOut)
def actualizar_concesionario(
    concesionario_id: UUID,
    concesionario: ConcesionarioCreate,
    db: Session = Depends(get_db),
):
    """
    Actualiza los datos de un concesionario existente.
    Retorna el concesionario modificado o 404 si no existe.
    """
    db_concesionario = concesionario_crud.actualizar_concesionario(
        db, concesionario_id, concesionario
    )
    if not db_concesionario:
        raise HTTPException(status_code=404, detail="Concesionario no encontrado")
    return db_concesionario


@router.delete("/{concesionario_id}")
def eliminar_concesionario(concesionario_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un concesionario de la base de datos.
    Retorna confirmación o 404 si no existe.
    """
    concesionario = db.query(Concesionario).filter_by(id=concesionario_id).first()
    if not concesionario:
        raise HTTPException(status_code=404, detail="Concesionario no encontrado")
    db.delete(concesionario)
    db.commit()
    return {"mensaje": "Concesionario eliminado correctamente"}
