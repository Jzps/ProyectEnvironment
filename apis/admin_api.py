from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.admin_schema import AdminCreate, AdminOut
from services.admin_service import AdminService
from crud import admin_crud
from uuid import UUID
from typing import List

router = APIRouter(
    prefix="/admin",
    tags=["Administradores"],
    responses={404: {"description": "No encontrado"}},
)


def get_db():
    """
    Provee una sesión de base de datos.
    Se usa como dependencia en los endpoints.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AdminOut, status_code=status.HTTP_201_CREATED)
def crear_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo administrador en el sistema.
    Retorna el objeto creado con su información.
    """
    service = AdminService(db)
    return service.crear_admin(admin)


@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    """
    Inicia sesión de un administrador.
    Verifica credenciales y retorna un mensaje de acceso.
    """
    service = AdminService(db)
    if service.login(username, password):
        return {"mensaje": f"Bienvenido {username}"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas"
    )


@router.get("/", response_model=List[AdminOut])
def listar_admins(db: Session = Depends(get_db)):
    """
    Lista todos los administradores registrados.
    Retorna una colección de administradores.
    """
    service = AdminService(db)
    return service.listar_admins()


@router.get("/{admin_id}", response_model=AdminOut)
def obtener_admin(admin_id: UUID, db: Session = Depends(get_db)):
    """
    Obtiene un administrador por su ID único.
    Lanza error 404 si no existe.
    """
    admin = db.query(admin_crud.Admin).filter_by(id=admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return admin


@router.delete("/{admin_id}")
def eliminar_admin(admin_id: UUID, db: Session = Depends(get_db)):
    """
    Elimina un administrador por su ID.
    Retorna un mensaje de confirmación si existe.
    """
    admin = admin_crud.eliminar_admin(db, admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin no encontrado")
    return {"mensaje": "Administrador eliminado correctamente"}
