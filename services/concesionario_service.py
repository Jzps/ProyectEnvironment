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

    def vender_auto(self, indice: int, usuario_id: UUID | None = None):
        autos = auto_crud.obtener_autos(self.db, disponibles_only=True)
        if not (0 <= indice - 1 < len(autos)):
            print("Índice inválido, no se pudo vender el auto.")
            return

        auto = autos[indice - 1]
        print(f"Auto seleccionado: {auto.marca} {auto.modelo} - ${auto.precio}")

        clientes = self.cliente_service.listar_clientes()
        if not clientes:
            print("No hay clientes registrados. Registre un cliente antes de vender.")
            return
        for c in clientes:
            print(f"{c.id}. {c.nombre} {c.apellido} - DNI: {c.dni}")
        cliente_id = UUID(input("Ingrese el ID del cliente comprador: "))
        cliente = next((c for c in clientes if c.id == cliente_id), None)
        if not cliente:
            print("Cliente inválido.")
            return

        vendedores = self.empleado_service.listar_vendedores()
        if not vendedores:
            print("No hay vendedores registrados.")
            return

        empleados = self.empleado_service.listar_empleados()
        emp_map = {e.id: e for e in empleados}

        for v in vendedores:
            emp = emp_map.get(v.empleado_id)
            if emp:
                print(f"{v.empleado_id}. {emp.nombre} {emp.apellido}")

        vendedor_id = UUID(input("Ingrese el ID del vendedor: "))
        vendedor_emp = emp_map.get(vendedor_id)
        if not vendedor_emp:
            print("Vendedor inválido.")
            return

        auto_crud.marcar_vendido(self.db, auto.id, usuario_id)

        factura = self.factura_service.crear_factura(
            FacturaCreate(
                fecha_emision=date.today(),
                cliente_id=cliente.id,
                empleado_id=vendedor_id,
                auto_id=auto.id,
                precio_carro_base=auto.precio,
                costo_mantenimiento=0.0,
                descuento=0.0,
                total=0.0,
                observaciones="Factura generada automáticamente al vender el auto",
            ),
            usuario_id,
        )

        print("\n--- FACTURA GENERADA ---")
        print(f"Factura ID: {factura.id}")
        print(f"Fecha: {factura.fecha_emision}")
        print(f"Cliente: {cliente.nombre} {cliente.apellido}")
        print(f"Vendedor: {vendedor_emp.nombre} {vendedor_emp.apellido}")
        print(f"Auto: {auto.marca} {auto.modelo} ({auto.tipo})")
        print(f"Precio: ${auto.precio}")
        print(f"Total: ${factura.total}")

    def dar_mantenimiento(self, indice: int, usuario_id: UUID | None = None):
        autos_all = auto_crud.obtener_autos(self.db, disponibles_only=False)
        if not (0 <= indice - 1 < len(autos_all)):
            print("Índice inválido, no se pudo dar mantenimiento.")
            return

        auto_db = autos_all[indice - 1]
        print(f"Auto seleccionado: {auto_db.marca} {auto_db.modelo}")

        tecnicos = self.empleado_service.listar_tecnicos()
        if not tecnicos:
            print("No hay técnicos registrados.")
            return

        empleados = self.empleado_service.listar_empleados()
        emp_map = {e.id: e for e in empleados}

        for t in tecnicos:
            emp = emp_map.get(t.empleado_id)
            if emp:
                print(f"{t.empleado_id}. {emp.nombre} {emp.apellido} - {t.tipo_carro}")

        tecnico_id = UUID(input("Ingrese el ID del técnico: "))
        if not any(t.empleado_id == tecnico_id for t in tecnicos):
            print("Técnico inválido.")
            return

        detalle = input("Detalle del mantenimiento: ")
        costo = float(input("Costo: "))

        mant = MantenimientoCreate(
            auto_id=auto_db.id,
            empleado_id=tecnico_id,
            fecha=date.today(),
            detalle=detalle,
            costo=costo,
        )
        self.mantenimiento_service.registrar_mantenimiento(mant, usuario_id)
        print(f"Mantenimiento registrado para {auto_db.marca} {auto_db.modelo}")
