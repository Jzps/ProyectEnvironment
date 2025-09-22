from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class AutoBase(BaseModel):
    """
    Esquema base para la entidad Auto.

    Atributos:
        marca (str): Marca del automóvil.
        modelo (str): Modelo del automóvil.
        precio (float): Precio del automóvil.
        tipo (str): Tipo o categoría del automóvil (por ejemplo, eléctrico, usado, etc.).
        extra (str | None): Información adicional u opcional del automóvil.
    """

    marca: str
    modelo: str
    precio: float
    tipo: str
    extra: str | None = None


class AutoCreate(AutoBase):
    """
    Esquema de entrada para la creación de un automóvil.

    Hereda de:
        AutoBase: Incluye los campos necesarios para registrar un automóvil.
    """

    pass


class AutoOut(AutoBase):
    """
    Esquema de salida para representar un automóvil en las respuestas de la API.

    Atributos adicionales:
        id (UUID): Identificador único del automóvil.
        vendido (bool): Indica si el automóvil ya fue vendido.
        id_usuario_creacion (UUID | None): Identificador del usuario que creó el registro.
        id_usuario_edicion (UUID | None): Identificador del usuario que realizó la última edición.
        fecha_creacion (datetime | None): Fecha y hora de creación del registro.
        fecha_actualizacion (datetime | None): Fecha y hora de la última actualización.
    """

    id: UUID
    vendido: bool
    id_usuario_creacion: UUID | None = None
    id_usuario_edicion: UUID | None = None
    fecha_creacion: datetime | None = None
    fecha_actualizacion: datetime | None = None

    class Config:
        """
        Configuración de Pydantic para habilitar la conversión de
        objetos ORM (por ejemplo, instancias de SQLAlchemy) a este esquema.
        """

        from_attributes = True
