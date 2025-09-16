from sqlalchemy.orm import Session
from database.entities import Admin
from schemas.admin_schema import AdminCreate


def crear_admin(db: Session, admin: AdminCreate):
    db_admin = Admin(username=admin.username, password=admin.password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def obtener_admin(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()
