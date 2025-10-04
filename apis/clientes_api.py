from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.cliente_schema import ClienteCreate, ClienteOut
from services.cliente_service import ClienteService
from crud import cliente_crud
from uuid import UUID
from typing import List

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"],
    responses={404: {"description": "No encontrado"}},
)


def get_db():
    """
    Provee una sesión de base de datos activa.
    Se usa como dependencia en los endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo cliente en la base de datos.
    Retorna los datos del cliente registrado.
    """
    service = ClienteService(db)
    return service.registrar_cliente(cliente)


@router.get("/", response_model=List[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    """
    Lista todos los clientes registrados.
    Devuelve una lista de objetos cliente.
    """
    service = ClienteService(db)
    return service.listar_clientes()


@router.get("/{cliente_id}", response_model=ClienteOut)
def obtener_cliente(cliente_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene la información de un cliente por su ID único.
    Lanza error 404 si no existe.
    """
    cliente = db.query(cliente_crud.Cliente).filter_by(id=cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


@router.put("/{cliente_id}", response_model=ClienteOut)
def actualizar_cliente(
    cliente_id: UUID, cliente: ClienteCreate, db: Session = Depends(get_db)
):
    """
    Actualiza los datos de un cliente existente.
    Retorna el cliente actualizado o error si no existe.
    """
    db_cliente = cliente_crud.actualizar_cliente(db, cliente_id, cliente)
    if not db_cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente


@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un cliente de la base de datos.
    Retorna confirmación o error si no existe.
    """
    service = ClienteService(db)
    eliminado = service.eliminar_cliente(cliente_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"mensaje": "Cliente eliminado con éxito"}
