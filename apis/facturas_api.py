from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from crud import factura_crud
from schemas.factura_schema import FacturaCreate, FacturaOut
from typing import List
from uuid import UUID

router = APIRouter(
    prefix="/facturas",
    tags=["Facturas"],
    responses={404: {"description": "No encontrado"}},
)


@router.post("/", response_model=FacturaOut, status_code=201)
def crear_factura(factura: FacturaCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva factura en el sistema.
    Retorna la factura recién registrada.
    """
    return factura_crud.crear_factura(db, factura)


@router.get("/", response_model=List[FacturaOut])
def listar_facturas(db: Session = Depends(get_db)):
    """
    Lista todas las facturas registradas.
    Retorna una lista de facturas con su información.
    """
    return factura_crud.obtener_facturas(db)


@router.get("/{factura_id}", response_model=FacturaOut)
def obtener_factura(factura_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene una factura específica por su ID.
    Retorna la factura encontrada o error 404 si no existe.
    """
    factura = factura_crud.obtener_factura_por_id(db, factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura


@router.delete("/{factura_id}")
def eliminar_factura(factura_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina una factura de la base de datos.
    Retorna confirmación o error 404 si no existe.
    """
    factura = factura_crud.eliminar_factura(db, factura_id)
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return {"mensaje": "Factura eliminada correctamente"}
