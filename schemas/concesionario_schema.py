from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ConcesionarioBase(BaseModel):
    """
    Esquema base para la entidad Concesionario.

    Atributos:
        nombre (str): Nombre del concesionario.
        direccion (str | None): Dirección del concesionario (opcional).
        telefono (str | None): Número de contacto del concesionario (opcional).
    """

    nombre: str
    direccion: str | None = None
    telefono: str | None = None


class ConcesionarioCreate(ConcesionarioBase):
    """
    Esquema de entrada para crear un concesionario.
    """

    pass


class ConcesionarioOut(ConcesionarioBase):
    """
    Esquema de salida para devolver un concesionario.
    """

    id: UUID
    fecha_creacion: datetime

    class Config:
        from_attributes = True  # ✅ Pydantic v2
