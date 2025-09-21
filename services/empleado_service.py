from database.config import SessionLocal
from crud import empleado_crud
from schemas import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate
from uuid import UUID


class EmpleadoService:
    def __init__(self, db=None):
        self.db = db or SessionLocal()

    def registrar_empleado(
        self, empleado: EmpleadoCreate, usuario_id: UUID | None = None
    ):
        return empleado_crud.crear_empleado(self.db, empleado, usuario_id)

    def listar_empleados(self):
        return empleado_crud.obtener_empleados(self.db)

    def registrar_vendedor(
        self, vendedor: VendedorCreate, usuario_id: UUID | None = None
    ):
        return empleado_crud.registrar_vendedor(self.db, vendedor, usuario_id)

    def listar_vendedores(self):
        return empleado_crud.obtener_vendedores(self.db)

    def registrar_tecnico(
        self, tecnico: MantenimientoEmpleadoCreate, usuario_id: UUID | None = None
    ):
        return empleado_crud.registrar_mantenimiento_empleado(
            self.db, tecnico, usuario_id
        )

    def listar_tecnicos(self):
        return empleado_crud.obtener_tecnicos(self.db)
