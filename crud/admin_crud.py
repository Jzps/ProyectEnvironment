import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from database.entities import Admin
from schemas.admin_schema import AdminCreate
from uuid import UUID


def crear_admin(db: Session, admin: AdminCreate, usuario_id: UUID | None = None):
    db_admin = Admin(
        id=uuid.uuid4(),
        username=admin.username,
        password=admin.password,
        id_usuario_creacion=usuario_id,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def obtener_admin(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()
