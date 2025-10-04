"""
Módulo principal de la API del Concesionario.

Este archivo inicializa la aplicación FastAPI, configura la base de datos
y registra los routers de las diferentes entidades del sistema:
clientes, empleados, autos, administradores, concesionarios, facturas y mantenimientos.

Ejecución
---------
python main.py

La documentación de la API estará disponible en:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
"""

from datetime import datetime
from typing import Dict

import uvicorn
from fastapi import FastAPI

from database import init_db
from apis import (
    clientes_router,
    empleados_router,
    autos_router,
    mantenimientos_router,
    admin_router,
    concesionario_router,
    facturas_router,
)

init_db()

app = FastAPI(
    title="API Concesionario",
    description=(
        "API para gestionar el concesionario de autos.\n\n"
        "Incluye módulos para clientes, empleados, autos, mantenimientos, "
        "administradores, concesionarios y facturas."
    ),
    version="1.0.0",
)


@app.get("/", response_model=Dict[str, str])
async def root():
    """
    Endpoint raíz de la API.

    Retorna un mensaje de bienvenida con información básica
    y un enlace a la documentación.
    """
    return {
        "mensaje": "Bienvenido a la API del Concesionario",
        "version": "1.0.0",
        "documentacion": "/docs",
    }


app.include_router(clientes_router)
app.include_router(empleados_router)
app.include_router(autos_router)
app.include_router(admin_router)
app.include_router(concesionario_router)
app.include_router(facturas_router)
app.include_router(mantenimientos_router)


@app.get("/estadisticas")
async def estadisticas():
    """
    Obtener estadísticas generales de la API.

    Actualmente retorna la fecha de consulta y un mensaje informativo.
    Futuras versiones mostrarán métricas reales del sistema.
    """
    return {
        "fecha_consulta": datetime.now().isoformat(),
        "info": "Próximamente: métricas reales de clientes, empleados, autos y mantenimientos",
    }


if __name__ == "__main__":
    print("Iniciando servidor FastAPI...")
    print("Documentación disponible en: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
