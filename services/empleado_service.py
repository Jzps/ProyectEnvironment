from database.config import SessionLocal
from crud import empleado_crud
from schemas import EmpleadoCreate, VendedorCreate, MantenimientoEmpleadoCreate

class EmpleadoService:
    def __init__(self):
        self.db = SessionLocal()

    def registrar_empleado(self, empleado: EmpleadoCreate):
        return empleado_crud.crear_empleado(self.db, empleado)

    def listar_empleados(self):
        return empleado_crud.obtener_empleados(self.db)

    def registrar_vendedor(self, vendedor: VendedorCreate):
        return empleado_crud.registrar_vendedor(self.db, vendedor)

    def listar_vendedores(self):
        return empleado_crud.obtener_vendedores(self.db)

    def registrar_tecnico(self, tecnico: MantenimientoEmpleadoCreate):
        return empleado_crud.registrar_mantenimiento_empleado(self.db, tecnico)

    def listar_tecnicos(self):
        return empleado_crud.obtener_tecnicos(self.db)
