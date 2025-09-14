from pydantic import BaseModel


class AdminBase(BaseModel):
    username: str
    password: str


class AdminCreate(AdminBase):
    pass


class AdminOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
