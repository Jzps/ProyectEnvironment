from database.config import SessionLocal
from crud import auto_crud
from schemas.auto_schema import AutoCreate
from services import (
    ClienteService,
    EmpleadoService,
    MantenimientoService,
    FacturaService,
)
from schemas import MantenimientoCreate, FacturaCreate
from datetime import date
from uuid import UUID


class Concesionario:
    """
    Servicio central para gestionar autos, clientes,
    empleados, ventas y mantenimientos.
    """

    def __init__(self, db=None):
        self.db = db or SessionLocal()
        self.cliente_service = ClienteService(self.db)
        self.empleado_service = EmpleadoService(self.db)
        self.mantenimiento_service = MantenimientoService(self.db)
        self.factura_service = FacturaService(self.db)

    def comprar_auto(self, auto, usuario_id: UUID | None = None):
        auto_schema = AutoCreate(
            marca=auto.marca,
            modelo=auto.modelo,
            precio=auto.precio,
            tipo=auto.__class__.__name__,
            extra=str(getattr(auto, "kilometraje", getattr(auto, "autonomia", None))),
        )
        auto_crud.crear_auto(self.db, auto_schema, usuario_id)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    def mostrar_autos(self):
        return auto_crud.obtener_autos(self.db, disponibles_only=True)

    def mostrar_autos_vendidos(self):
        return auto_crud.obtener_autos_vendidos(self.db)

    def vender_auto(self, auto_id: UUID, usuario_id: UUID | None = None):
        """
        Vende un auto disponible por su UUID.
        """
        auto = auto_crud.obtener_auto_por_id(self.db, auto_id)
        if not auto or auto.vendido:
            return None

        auto_crud.marcar_vendido(self.db, auto.id, usuario_id)
        return auto

    def dar_mantenimiento(self, auto_id: UUID, usuario_id: UUID | None = None):
        auto = auto_crud.obtener_auto_por_id(self.db, auto_id)
        if not auto:
            return None
        # Aquí implementarías lógica de mantenimiento con técnicos, similar a lo que ya tienes.
        return auto
