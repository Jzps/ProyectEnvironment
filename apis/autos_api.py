from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from services import Concesionario
from autos.tipos import AutoNuevo, AutoUsado, AutoElectrico
from crud import auto_crud
from schemas.auto_schema import AutoCreate, AutoOut
from uuid import UUID
from typing import List

router = APIRouter(
    prefix="/autos",
    tags=["Autos"],
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


@router.post("/comprar")
def comprar_auto(
    tipo: str,
    marca: str,
    modelo: str,
    precio: float,
    kilometraje: int | None = None,
    autonomia: int | None = None,
    db: Session = Depends(get_db),
):
    """
    Registra un nuevo auto en el concesionario.
    Soporta autos nuevos, usados y eléctricos con sus atributos.
    """
    concesionario = Concesionario(db)
    tipo_normalizado = tipo.lower()

    if tipo_normalizado == "nuevo":
        auto = AutoNuevo(marca, modelo, precio)
    elif tipo_normalizado == "usado":
        if kilometraje is None:
            raise HTTPException(
                status_code=400, detail="Debes enviar el kilometraje para un auto usado"
            )
        auto = AutoUsado(marca, modelo, precio, kilometraje)
    elif tipo_normalizado == "electrico":
        if autonomia is None:
            raise HTTPException(
                status_code=400,
                detail="Debes enviar la autonomía para un auto eléctrico",
            )
        auto = AutoElectrico(marca, modelo, precio, autonomia)
    else:
        raise HTTPException(
            status_code=400,
            detail="Tipo de auto no válido. Usa: nuevo, usado, electrico",
        )

    concesionario.comprar_auto(auto)
    return {
        "mensaje": f"Auto {marca} {modelo} registrado con éxito como {tipo_normalizado}"
    }


@router.get("/", response_model=List[AutoOut])
def listar_autos(db: Session = Depends(get_db)):
    """
    Lista todos los autos disponibles.
    Solo muestra aquellos que no han sido vendidos.
    """
    concesionario = Concesionario(db)
    return concesionario.mostrar_autos()


@router.get("/{auto_id}", response_model=AutoOut)
def obtener_auto(auto_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene la información de un auto por su ID único.
    Lanza un error 404 si no existe.
    """
    auto = db.query(auto_crud.Auto).filter_by(id=auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto


@router.post("/vender/{auto_id}")
def vender_auto(auto_id: UUID, db: Session = Depends(get_db)):
    """
    Marca un auto como vendido usando su ID.
    Retorna la información básica del auto vendido.
    """
    auto = auto_crud.marcar_vendido(db, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado o ya vendido")
    return {
        "mensaje": f"Auto {auto.marca} {auto.modelo} vendido con éxito",
        "auto_id": str(auto.id),
    }


@router.get("/vendidos", response_model=List[AutoOut])
def listar_autos_vendidos(db: Session = Depends(get_db)):
    """
    Lista todos los autos ya vendidos.
    Incluye su información completa.
    """
    concesionario = Concesionario(db)
    return concesionario.mostrar_autos_vendidos()


@router.put("/{auto_id}", response_model=AutoOut)
def actualizar_auto(auto_id: UUID, auto: AutoCreate, db: Session = Depends(get_db)):
    """
    Actualiza los datos de un auto por su ID.
    Si no existe, devuelve error 404.
    """
    db_auto = auto_crud.actualizar_auto(db, auto_id, auto)
    if not db_auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return db_auto


@router.delete("/{auto_id}")
def eliminar_auto(auto_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un auto del sistema usando su ID.
    Devuelve confirmación si el auto existía.
    """
    auto = auto_crud.eliminar_auto(db, auto_id)
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return {"mensaje": "Auto eliminado correctamente"}
