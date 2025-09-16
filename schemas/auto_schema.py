from pydantic import BaseModel


class AutoBase(BaseModel):
    marca: str
    modelo: str
    precio: float
    tipo: str
    extra: str | None = None


class AutoCreate(AutoBase):
    pass


class AutoOut(AutoBase):
    id: int

    class Config:
        orm_mode = True
