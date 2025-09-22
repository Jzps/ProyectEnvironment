import sys
from sqlalchemy import text
from database.config import DATABASE_URL, engine


def test_connection():
    """
    Prueba la conexión a la base de datos PostgreSQL con SQLAlchemy.
    Muestra la URL, versión de PostgreSQL, base de datos y tablas del esquema.
    Si la conexión falla imprime el error.

    Returns:
        True si la conexión fue exitosa, False en caso contrario.
    """

    print("=== PRUEBA DE CONEXION A POSTGRESQL (NEON) ===\n")
    print(f"URL de conexion: {DATABASE_URL}")
    print()

    try:

        with engine.connect() as connection:
            print("[OK] Conexion exitosa a PostgreSQL!")

            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()
            print(f"[OK] Version de PostgreSQL: {version[0]}")

            result = connection.execute(text("SELECT current_database()"))
            db_name = result.fetchone()
            print(f"[OK] Conectado a la base de datos: {db_name[0]}")

            print("\nTablas disponibles en 'public':")
            result = connection.execute(
                text(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
                )
            )
            tables = result.fetchall()
            if tables:
                for table in tables:
                    print(f"  - {table[0]}")
            else:
                print("  (No hay tablas creadas aún)")

    except Exception as e:
        print(f"[ERROR] Error de conexion: {e}")
        print("\nPosibles soluciones:")
        print("1. Verificar que la URL de conexion en .env sea correcta")
        print("2. Verificar que la base de datos este activa en Neon")
        print("3. Revisar credenciales y permisos")
        print("4. Confirmar que hay conexion a internet")
        return False

    return True


if __name__ == "__main__":

    print("Iniciando prueba de conexion...\n")
    if test_connection():
        print("\n[SUCCESS] Conexion realizada con exito")
    else:
        sys.exit(1)
