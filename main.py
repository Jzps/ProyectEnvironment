import warnings

warnings.filterwarnings("ignore", category=UserWarning)

from database import SessionLocal, init_db
from services import (
    Concesionario,
    ClienteService,
    EmpleadoService,
    MantenimientoService,
    FacturaService,
)
from services.admin_service import AdminService
from autos.tipos import AutoNuevo, AutoUsado, AutoElectrico
from schemas import (
    ClienteCreate,
    EmpleadoCreate,
    VendedorCreate,
    MantenimientoEmpleadoCreate,
    MantenimientoCreate,
    FacturaCreate,
    AdminCreate,
)
from datetime import date


init_db()


def menu_clientes():
    cliente_service = ClienteService()
    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1. Registrar Cliente")
        print("2. Listar Clientes")
        print("3. Eliminar Cliente")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")

            cliente = ClienteCreate(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                correo=correo,
                telefono=telefono,
                direccion=direccion,
            )
            cliente_service.registrar_cliente(cliente)
            print("Cliente registrado con éxito.")

        elif opcion == "2":
            clientes = cliente_service.listar_clientes()
            for c in clientes:
                print(f"{c.id}. {c.nombre} {c.apellido} - DNI: {c.dni}")

        elif opcion == "3":
            cliente_id = int(input("ID de cliente a eliminar: "))
            cliente_service.eliminar_cliente(cliente_id)
            print("Cliente eliminado (si existía).")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def menu_empleados():
    empleado_service = EmpleadoService()
    while True:
        print("\n--- MENÚ EMPLEADOS ---")
        print("1. Registrar Empleado")
        print("2. Listar Empleados")
        print("3. Registrar Vendedor")
        print("4. Registrar Técnico")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            fecha_contratacion = date.today()

            empleado = EmpleadoCreate(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                correo=correo,
                telefono=telefono,
                fecha_contratacion=fecha_contratacion,
            )
            empleado_service.registrar_empleado(empleado)
            print("Empleado registrado.")

        elif opcion == "2":
            empleados = empleado_service.listar_empleados()
            if not empleados:
                print("No hay empleados registrados.")
            else:
                for e in empleados:
                    print(f"{e.id}. {e.nombre} {e.apellido} - DNI: {e.dni}")

        elif opcion == "3":
            empleado_id = int(input("ID de empleado a registrar como vendedor: "))
            vendedor = VendedorCreate(empleado_id=empleado_id)
            empleado_service.registrar_vendedor(vendedor)
            print("Empleado registrado como Vendedor.")

        elif opcion == "4":
            empleado_id = int(input("ID de empleado a registrar como técnico: "))
            tipo_carro = input(
                "Tipo de carro que atiende (AutoNuevo, AutoUsado, AutoElectrico): "
            )
            tecnico = MantenimientoEmpleadoCreate(
                empleado_id=empleado_id, tipo_carro=tipo_carro
            )
            empleado_service.registrar_tecnico(tecnico)
            print("Empleado registrado como Técnico de Mantenimiento.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


def menu_mantenimientos():
    mantenimiento_service = MantenimientoService()
    while True:
        print("\n--- MENÚ MANTENIMIENTOS ---")
        print("1. Listar Mantenimientos")
        print("2. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mantenimientos = mantenimiento_service.listar_mantenimientos()
            if not mantenimientos:
                print("No hay mantenimientos registrados.")
            else:
                for m in mantenimientos:
                    print(
                        f"{m.id}. Auto: {m.auto_id}, Técnico: {m.empleado_id}, {m.detalle}, ${m.costo}"
                    )

        elif opcion == "2":
            break
        else:
            print("Opción inválida.")


def menu_facturas():
    factura_service = FacturaService()
    while True:
        print("\n--- MENÚ FACTURAS ---")
        print("1. Crear Factura")
        print("2. Listar Facturas")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cliente_id = int(input("ID Cliente: "))
            empleado_id = int(input("ID Vendedor: "))
            auto_id = int(input("ID Auto: "))
            precio_base = float(input("Precio base del auto: "))
            descuento = float(input("Descuento: "))
            observaciones = input("Observaciones: ")

            factura = FacturaCreate(
                fecha_emision=date.today(),
                cliente_id=cliente_id,
                empleado_id=empleado_id,
                auto_id=auto_id,
                precio_carro_base=precio_base,
                costo_mantenimiento=0.0,
                descuento=descuento,
                total=0.0,
                observaciones=observaciones,
            )
            factura_db = factura_service.crear_factura(factura)
            if factura_db:
                print(f"Factura creada. Total = ${factura_db.total}")

        elif opcion == "2":
            facturas = factura_service.listar_facturas()
            for f in facturas:
                print(
                    f"{f.id}. Cliente {f.cliente_id} Auto {f.auto_id} Total: ${f.total}"
                )

        elif opcion == "3":
            break
        else:
            print("Opción inválida.")


def menu():
    concesionario = Concesionario()

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Concesionario (Autos)")
        print("2. Clientes")
        print("3. Empleados")
        print("4. Mantenimientos")
        print("5. Facturas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                print("\n--- MENÚ CONCESIONARIO ---")
                print("1. Comprar Auto")
                print("2. Vender Auto")
                print("3. Mostrar Autos")
                print("4. Dar Mantenimiento")
                print("5. Mostrar Autos Vendidos")
                print("6. Volver")

                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    print("\nTipos de Auto:")
                    print("1. Nuevo")
                    print("2. Usado")
                    print("3. Eléctrico")

                    tipo = input("Seleccione el tipo de auto: ")
                    marca = input("Ingrese la marca: ")
                    modelo = input("Ingrese el modelo: ")
                    precio = float(input("Ingrese el precio: "))

                    if tipo == "1":
                        auto_obj = AutoNuevo(marca, modelo, precio)
                    elif tipo == "2":
                        kilometraje = int(input("Ingrese el kilometraje: "))
                        auto_obj = AutoUsado(marca, modelo, precio, kilometraje)
                    elif tipo == "3":
                        autonomia = int(input("Ingrese la autonomía (km): "))
                        auto_obj = AutoElectrico(marca, modelo, precio, autonomia)
                    else:
                        print("Tipo inválido.")
                        continue

                    concesionario.comprar_auto(auto_obj)

                elif subopcion == "2":
                    autos = concesionario.mostrar_autos()
                    if not autos:
                        continue
                    auto_id = int(input("Ingrese el número del auto a vender: "))
                    concesionario.vender_auto(auto_id)

                elif subopcion == "3":
                    concesionario.mostrar_autos()

                elif subopcion == "4":
                    autos = concesionario.mostrar_autos()
                    if not autos:
                        continue
                    auto_id = int(
                        input("Ingrese el número del auto para dar mantenimiento: ")
                    )
                    concesionario.dar_mantenimiento(auto_id)

                elif subopcion == "5":
                    concesionario.mostrar_autos_vendidos()

                elif subopcion == "6":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_empleados()
        elif opcion == "4":
            menu_mantenimientos()
        elif opcion == "5":
            menu_facturas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    db = SessionLocal()
    admin_service = AdminService(db)

    admins = admin_service.listar_admins()

    if not admins:
        print(" No existe ningún admin. Debe registrar uno antes de continuar.")
        username = input("Nuevo usuario admin: ")
        password = input("Nueva contraseña: ")

        nuevo_admin = AdminCreate(username=username, password=password)
        admin_service.crear_admin(nuevo_admin)
        print(" Admin creado con éxito. Vuelva a iniciar el programa.")
    else:
        print("=== LOGIN ADMIN ===")
        username = input("Usuario: ")
        password = input("Contraseña: ")

        if admin_service.login(username, password):
            print(f" Bienvenido {username}")
            menu()
        else:
            print(" Credenciales incorrectas. Saliendo...")
