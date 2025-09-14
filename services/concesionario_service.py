from database.config import SessionLocal
from crud import auto_crud
from schemas.auto_schema import AutoCreate
from autos import AutoNuevo, AutoUsado, AutoElectrico
from services import ClienteService, EmpleadoService, MantenimientoService
from schemas import MantenimientoCreate
from datetime import date


class Concesionario:
    def __init__(self):
        self.db = SessionLocal()
        self.cliente_service = ClienteService()
        self.empleado_service = EmpleadoService()
        self.mantenimiento_service = MantenimientoService()

    def comprar_auto(self, auto):
        auto_schema = AutoCreate(
            marca=auto.marca,
            modelo=auto.modelo,
            precio=auto.precio,
            tipo=auto.__class__.__name__,
            extra=str(getattr(auto, "kilometraje", getattr(auto, "autonomia", None))),
        )
        auto_crud.crear_auto(self.db, auto_schema)
        print(f"Se ha comprado: {auto.mostrar_info()}")

    def mostrar_autos(self):
        autos = auto_crud.obtener_autos(self.db, disponibles_only=True)
        if not autos:
            print("No hay autos disponibles.")
            return []
        for i, a in enumerate(autos, start=1):
            print(f"{i}. {a.marca} {a.modelo} ({a.tipo}) - ${a.precio}")
        return autos

    def mostrar_autos_vendidos(self):
        autos = auto_crud.obtener_autos_vendidos(self.db)
        if not autos:
            print("No hay autos vendidos.")
            return
        print("\n--- AUTOS VENDIDOS ---")
        for a in autos:
            print(f"{a.id}. {a.marca} {a.modelo} ({a.tipo}) - ${a.precio}")

    def vender_auto(self, indice: int):
        autos = auto_crud.obtener_autos(self.db, disponibles_only=True)
        if not (0 <= indice - 1 < len(autos)):
            print("Índice inválido, no se pudo vender el auto.")
            return

        auto = autos[indice - 1]
        print(f"Auto seleccionado: {auto.marca} {auto.modelo} - ${auto.precio}")

        clientes = self.cliente_service.listar_clientes()
        if not clientes:
            print(" No hay clientes registrados. Registre un cliente antes de vender.")
            return
        print("\n--- CLIENTES ---")
        for c in clientes:
            print(f"{c.id}. {c.nombre} {c.apellido} - DNI: {c.dni}")
        cliente_id = int(input("Ingrese el ID del cliente comprador: "))
        if not any(c.id == cliente_id for c in clientes):
            print("Cliente inválido.")
            return

        vendedores = self.empleado_service.listar_vendedores()
        if not vendedores:
            print(
                " No hay vendedores registrados. Registre un vendedor antes de vender."
            )
            return

        empleados = self.empleado_service.listar_empleados()
        emp_map = {e.id: e for e in empleados}

        print("\n--- VENDEDORES ---")
        for v in vendedores:
            emp = emp_map.get(v.empleado_id)
            if emp:
                print(f"{v.empleado_id}. {emp.nombre} {emp.apellido}")
            else:
                print(f"{v.empleado_id}. (Empleado ID {v.empleado_id})")

        vendedor_id = int(input("Ingrese el ID del vendedor: "))
        if not any(v.empleado_id == vendedor_id for v in vendedores):
            print("Vendedor inválido.")
            return

        auto_crud.marcar_vendido(self.db, auto.id)
        print(
            f" Auto '{auto.marca} {auto.modelo}' marcado como vendido. Genere la factura desde el menú de facturas."
        )

    def dar_mantenimiento(self, indice: int):
        autos_all = auto_crud.obtener_autos(self.db, disponibles_only=False)
        if not autos_all:
            print("No hay autos registrados para mantenimiento.")
            return

        if not (0 <= indice - 1 < len(autos_all)):
            print("Índice inválido, no se pudo dar mantenimiento.")
            return

        auto_db = autos_all[indice - 1]
        print(
            f"Auto seleccionado: {auto_db.marca} {auto_db.modelo} (vendido={auto_db.vendido})"
        )

        tecnicos = self.empleado_service.listar_tecnicos()
        if not tecnicos:
            print(" No hay técnicos de mantenimiento registrados. Registre uno antes.")
            return

        empleados = self.empleado_service.listar_empleados()
        emp_map = {e.id: e for e in empleados}

        print("\n--- TÉCNICOS DISPONIBLES ---")
        for t in tecnicos:
            emp = emp_map.get(t.empleado_id)
            if emp:
                print(
                    f"{t.empleado_id}. {emp.nombre} {emp.apellido} - Tipo: {t.tipo_carro}"
                )
            else:
                print(
                    f"{t.empleado_id}. (Empleado ID {t.empleado_id}) - Tipo: {t.tipo_carro}"
                )

        tecnico_id = int(input("Ingrese el ID del técnico a asignar: "))
        if not any(t.empleado_id == tecnico_id for t in tecnicos):
            print("Técnico inválido.")
            return

        detalle = input("Detalle del mantenimiento: ")
        costo = float(input("Costo del mantenimiento: "))
        fecha = date.today()

        mant = MantenimientoCreate(
            auto_id=auto_db.id,
            empleado_id=tecnico_id,
            fecha=fecha,
            detalle=detalle,
            costo=costo,
            factura_id=None,
        )
        self.mantenimiento_service.registrar_mantenimiento(mant)
        print(
            f" Mantenimiento registrado para {auto_db.marca} {auto_db.modelo} (${costo})."
        )
