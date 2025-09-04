from database.database import init_db
from services.concesionario import Concesionario
from autos.tipos import AutoNuevo, AutoUsado, AutoElectrico

# Crear tablas
init_db()

def menu():
    concesionario = Concesionario()

    while True:
        print("\n--- MENÚ CONCESIONARIO ---")
        print("1. Comprar Auto")
        print("2. Vender Auto")
        print("3. Mostrar Autos")
        print("4. Dar Mantenimiento")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
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

        elif opcion == "2":
            concesionario.mostrar_autos()
            auto_id = int(input("Ingrese el número del auto a vender: "))
            concesionario.vender_auto(auto_id)

        elif opcion == "3":
            concesionario.mostrar_autos()

        elif opcion == "4":
            concesionario.mostrar_autos()
            auto_id = int(input("Ingrese el número del auto para dar mantenimiento: "))
            concesionario.dar_mantenimiento(auto_id)

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    menu()
