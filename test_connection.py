import sys
from sqlalchemy import text
from database.config import DATABASE_URL, engine


def test_connection():
    """
    Prueba la conexión a la base de datos PostgreSQL usando SQLAlchemy.

    Flujo de la función:
    1. Muestra la URL de conexión configurada.
    2. Intenta conectarse a la base de datos usando engine.connect().
    3. Si la conexión es exitosa:
       - Imprime la versión de PostgreSQL.
       - Muestra el nombre de la base de datos conectada.
       - Lista todas las tablas existentes en el esquema 'public'.
    4. Si ocurre un error de conexión:
       - Muestra el error y posibles soluciones.
       - Retorna False.
    
    Retorna:
        True si la conexión fue exitosa, False en caso de error.
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
    """
    Bloque principal de ejecución del script.

    Flujo:
    1. Imprime un mensaje inicial indicando que se iniciará la prueba de conexión.
    2. Llama a test_connection().
       - Si la conexión es exitosa, imprime mensaje de éxito.
       - Si falla, termina el programa con código de salida 1.
    """
    
    print("Iniciando prueba de conexion...\n")
    if test_connection():
        print("\n[SUCCESS] Conexion realizada con exito")
    else:
        sys.exit(1)
