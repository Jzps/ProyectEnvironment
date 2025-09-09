from pydantic import BaseModel

class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    dni: str
    correo: str | None = None
    telefono: str | None = None
    direccion: str | None = None

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id: int

    class Config:
        orm_mode = True
