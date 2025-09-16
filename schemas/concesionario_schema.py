from pydantic import BaseModel


class ConcesionarioBase(BaseModel):
    nombre: str
    ubicacion: str | None = None
    telefono: str | None = None


class ConcesionarioCreate(ConcesionarioBase):
    pass


class ConcesionarioOut(ConcesionarioBase):
    id: int

    class Config:
        orm_mode = True
