"""
Script principal del concesionario.

Inicializa la base de datos, gestiona la sesión y muestra el menú principal.
Incluye submenús para clientes, empleados, autos y mantenimientos.
Si no existe administrador registrado, permite crear uno al inicio.
"""

from database import SessionLocal, init_db
from services import (
    Concesionario,
    ClienteService,
    EmpleadoService,
    MantenimientoService,
)
from services.admin_service import AdminService
from autos.tipos import AutoNuevo, AutoUsado, AutoElectrico
from schemas import (
    ClienteCreate,
    EmpleadoCreate,
    VendedorCreate,
    MantenimientoEmpleadoCreate,
    AdminCreate,
)
from datetime import date

init_db()
db = SessionLocal()


def menu_clientes(db):
    """
    Menú para gestionar clientes.

    Permite registrar, listar y eliminar clientes mediante ClienteService.
    El menú se ejecuta en bucle hasta que el usuario decida volver.
    """

    cliente_service = ClienteService(db)
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
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(f"{c.id}. {c.nombre} {c.apellido} - DNI: {c.dni}")

        elif opcion == "3":
            clientes = cliente_service.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                print("\n--- LISTA DE CLIENTES ---")
                for i, c in enumerate(clientes, start=1):
                    print(f"{i}. {c.nombre} {c.apellido} - DNI: {c.dni}")

                try:
                    seleccion = int(
                        input("Seleccione el número del cliente a eliminar: ")
                    )
                    if 1 <= seleccion <= len(clientes):
                        cliente = clientes[seleccion - 1]
                        cliente_service.eliminar_cliente(
                            cliente.id
                        )  # Pasamos el UUID real
                        print(
                            f"Cliente {cliente.nombre} {cliente.apellido} eliminado con éxito."
                        )
                    else:
                        print("Selección inválida.")
                except ValueError:
                    print("Entrada inválida. Debe ser un número.")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def menu_empleados(db):
    """
    Menú para gestionar empleados.

    Permite registrar empleados, listarlos y asignarlos como vendedores o técnicos.
    Se ejecuta en bucle hasta que el usuario decida volver.
    """

    empleado_service = EmpleadoService(db)
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
            empleados = empleado_service.listar_empleados()
            vendedores = empleado_service.listar_vendedores()
            ids_vendedores = {v.empleado_id for v in vendedores}

            disponibles = [e for e in empleados if e.id not in ids_vendedores]

            if not disponibles:
                print("No hay empleados disponibles para registrar como vendedores.")
            else:
                print("\n--- EMPLEADOS DISPONIBLES ---")
                for i, e in enumerate(disponibles, start=1):
                    print(f"{i}. {e.nombre} {e.apellido} - DNI: {e.dni}")

                opcion = int(input("Seleccione el número del empleado: "))
                if 1 <= opcion <= len(disponibles):
                    empleado = disponibles[opcion - 1]
                    vendedor = VendedorCreate(empleado_id=empleado.id)
                    empleado_service.registrar_vendedor(vendedor)
                    print(
                        f"Empleado {empleado.nombre} {empleado.apellido} registrado como Vendedor."
                    )
                else:
                    print("Opción inválida.")

        elif opcion == "4":
            empleados = empleado_service.listar_empleados()
            tecnicos = empleado_service.listar_tecnicos()
            ids_tecnicos = {t.empleado_id for t in tecnicos}

            disponibles = [e for e in empleados if e.id not in ids_tecnicos]

            if not disponibles:
                print("No hay empleados disponibles para registrar como técnicos.")
            else:
                print("\n--- EMPLEADOS DISPONIBLES ---")
                for i, e in enumerate(disponibles, start=1):
                    print(f"{i}. {e.nombre} {e.apellido} - DNI: {e.dni}")

                opcion = int(input("Seleccione el número del empleado: "))
                if 1 <= opcion <= len(disponibles):
                    empleado = disponibles[opcion - 1]
                    tipo_carro = input(
                        "Tipo de carro que atiende (AutoNuevo, AutoUsado, AutoElectrico): "
                    )
                    tecnico = MantenimientoEmpleadoCreate(
                        empleado_id=empleado.id, tipo_carro=tipo_carro
                    )
                    empleado_service.registrar_tecnico(tecnico)
                    print(
                        f"Empleado {empleado.nombre} {empleado.apellido} registrado como Técnico de Mantenimiento."
                    )
                else:
                    print("Opción inválida.")

        elif opcion == "5":
            break
        else:
            print("Opción inválida.")


def menu_mantenimientos(db):
    """
    Menú para gestionar mantenimientos de autos.

    Permite listar los mantenimientos registrados.
    Se repite en bucle hasta que el usuario decida volver.
    """

    mantenimiento_service = MantenimientoService(db)
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


def menu(db):
    """
    Menú principal del sistema.

    Integra los submenús de autos, clientes, empleados y mantenimientos.
    Se mantiene en bucle hasta que el usuario decide salir.
    """

    concesionario = Concesionario(db)

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Concesionario (Autos)")
        print("2. Clientes")
        print("3. Empleados")
        print("4. Mantenimientos")
        print("5. Salir")

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
            menu_clientes(db)
        elif opcion == "3":
            menu_empleados(db)
        elif opcion == "4":
            menu_mantenimientos(db)
        elif opcion == "5":
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
            menu(db)
        else:
            print(" Credenciales incorrectas. Saliendo...")
