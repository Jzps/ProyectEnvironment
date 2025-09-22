"""
Script principal de la aplicación del concesionario.

Proporciona menús interactivos para:
- Gestionar clientes: registrar, listar y eliminar.
- Gestionar empleados: registrar empleados, vendedores y técnicos.
- Gestionar autos: comprar, vender, mostrar y dar mantenimiento.
- Gestionar mantenimientos: listar mantenimientos registrados.
- Control de acceso: login de administrador.

Este script inicializa la base de datos, crea una sesión de SQLAlchemy
y ejecuta el menú principal interactivo basado en la entrada del usuario.

Funciones principales:
- menu_clientes(db): Menú para registrar, listar y eliminar clientes.
- menu_empleados(db): Menú para registrar empleados, vendedores y técnicos.
- menu_mantenimientos(db): Menú para listar mantenimientos.
- menu(db): Menú principal del sistema que integra todos los submenús.

Al inicio del programa, verifica si existe algún administrador. Si no, 
permite crear uno antes de acceder al sistema.
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

    Opciones:
    1. Registrar Cliente:
       - Solicita nombre, apellido, DNI, correo, teléfono y dirección.
       - Crea un Cliente usando ClienteService.
    2. Listar Clientes:
       - Muestra todos los clientes registrados con ID, nombre, apellido y DNI.
    3. Eliminar Cliente:
       - Solicita el ID del cliente y lo elimina si existe.
    4. Volver:
       - Sale del menú de clientes.
    
    El menú se mantiene en un bucle hasta que el usuario elige volver.
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
            cliente_id = int(input("ID de cliente a eliminar: "))
            cliente_service.eliminar_cliente(cliente_id)
            print("Cliente eliminado (si existía).")

        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


def menu_empleados(db):
    """
    Menú para gestionar empleados.

    Opciones:
    1. Registrar Empleado:
       - Solicita nombre, apellido, DNI, correo, teléfono.
       - La fecha de contratación se toma como la fecha actual.
       - Crea un empleado usando EmpleadoService.
    2. Listar Empleados:
       - Muestra todos los empleados con ID, nombre, apellido y DNI.
    3. Registrar Vendedor:
       - Lista empleados disponibles que no sean vendedores.
       - Permite asignar un empleado como vendedor.
    4. Registrar Técnico:
       - Lista empleados disponibles que no sean técnicos.
       - Permite asignar un empleado como técnico y definir el tipo de carro que atiende.
    5. Volver:
       - Sale del menú de empleados.

    El menú se mantiene en un bucle hasta que el usuario elige volver.
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

    Opciones:
    1. Listar Mantenimientos:
       - Muestra todos los mantenimientos registrados con ID, auto, técnico, detalle y costo.
    2. Volver:
       - Sale del menú de mantenimientos.

    El menú se mantiene en un bucle hasta que el usuario elige volver.
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

    Opciones:
    1. Concesionario (Autos):
       - Comprar Auto:
           * Selección de tipo de auto: Nuevo, Usado, Eléctrico.
           * Solicita datos según tipo y registra el auto.
       - Vender Auto:
           * Muestra autos disponibles.
           * Selección de cliente y vendedor.
           * Marca auto como vendido y genera factura.
       - Mostrar Autos Disponibles.
       - Dar Mantenimiento:
           * Selección de auto y técnico.
           * Registra mantenimiento con detalle y costo.
       - Mostrar Autos Vendidos.
    2. Clientes:
       - Llama a menu_clientes(db).
    3. Empleados:
       - Llama a menu_empleados(db).
    4. Mantenimientos:
       - Llama a menu_mantenimientos(db).
    5. Salir:
       - Termina la ejecución del programa.

    Mantiene un bucle hasta que el usuario decide salir.
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
    """
    Punto de entrada del programa.

    Flujo:
    1. Inicializa la base de datos y la sesión.
    2. Verifica si existe al menos un administrador.
       - Si no hay, permite crear uno.
    3. Solicita login de administrador.
       - Si las credenciales son correctas, llama a menu(db).
       - Si no, termina la ejecución.
    """
    
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
