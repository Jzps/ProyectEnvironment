---

# 🚗 Concesionario de Autos en Python (con API FastAPI)

Este proyecto es un **sistema completo de gestión para un concesionario de autos**, desarrollado en **Python** con **FastAPI**, **SQLAlchemy** y **PostgreSQL (NeonDB)**.

Permite **registrar, vender, dar mantenimiento y administrar autos, clientes, empleados, facturas y mantenimientos**, tanto desde consola como mediante **endpoints RESTful documentados con Swagger UI**.

---

## 📂 Estructura del Proyecto

```bash
ProyectEnvironment/
│── autos/                   # Clases que representan los distintos tipos de autos
│   ├── base.py
│   ├── tipos.py
│
│── crud/                    # Operaciones CRUD directas sobre la base de datos
│   ├── admin_crud.py
│   ├── auto_crud.py
│   ├── cliente_crud.py
│   ├── concesionario_crud.py
│   ├── empleado_crud.py
│   ├── especialidad_crud.py
│   ├── factura_crud.py
│   ├── mantenimiento_crud.py
│
│── database/                # Configuración y entidades de la base de datos
│   ├── base.py
│   ├── config.py
│   ├── db.py
│   ├── init_db.py
│   └── entities/            # Definición de modelos (tablas)
│
│── schemas/                 # Esquemas con Pydantic (validación de datos)
│   ├── admin_schema.py
│   ├── auto_schema.py
│   ├── cliente_schema.py
│   ├── concesionario_schema.py
│   ├── empleado_schema.py
│   ├── especialidad_schema.py
│   ├── factura_schema.py
│   ├── mantenimiento_schema.py
│
│── services/                # Lógica de negocio (intermediarios entre CRUD y main)
│   ├── admin_service.py
│   ├── cliente_service.py
│   ├── concesionario_service.py
│   ├── empleado_service.py
│   ├── factura_service.py
│   ├── mantenimiento_service.py
│
│── api/                     # Endpoints REST con FastAPI
│   ├── admin_api.py
│   ├── autos_api.py
│   ├── clientes_api.py
│   ├── empleados_api.py
│   ├── mantenimientos_api.py
│
│── main.py                  # Menú principal en consola
│── reset_db.py              # Script opcional para reiniciar tablas
│── test_connection.py       # Prueba de conexión con la base de datos
│── requirements.txt         # Dependencias necesarias
│── README.md                # Documentación del proyecto
```

---

## ⚙️ Requisitos Previos

* **Python 3.10+**
* **PostgreSQL** (se recomienda NeonDB en la nube)
* Librerías listadas en `requirements.txt`

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución del Proyecto

### 🌐 Modo API (FastAPI)

1. Levanta el servidor FastAPI:

   ```bash
   uvicorn main:app --reload
   ```

2. Abre la documentación interactiva:

   ```
   http://localhost:8000/docs
   ```

Ahí podrás probar todos los endpoints de:

* `/admin`
* `/autos`
* `/clientes`
* `/empleados`
* `/mantenimientos`
* `/facturas`
* `/concesinarios`

Cada uno incluye operaciones **GET, POST, PUT, DELETE** documentadas automáticamente.

---

## 🧠 Lógica de Negocio

* **Autos:**
  Representados por clases (`AutoNuevo`, `AutoUsado`, `AutoElectrico`) y administrados vía `auto_crud`.

* **Clientes y Empleados:**
  Gestión completa con validación (`cliente_service`, `empleado_service`).

* **Ventas:**
  Al vender un auto se marca como vendido y se **genera automáticamente una factura** con datos del cliente, vendedor y auto.

* **Mantenimientos:**
  Se asigna un técnico y se guarda el detalle y costo.
  En la versión actual, **ya no se requiere el `factura_id`** (se eliminó el campo de la tabla y del modelo para evitar errores al crear mantenimientos).

* **Login de Administradores:**
  El sistema incluye un **módulo de login** que permite validar credenciales antes de usar el sistema o acceder al panel API.

---

## 👨‍💻 Autores

* Juan Pablo Gutiérrez Vargas
* Juan Felipe Ospina Agudelo

---

## 📜 Licencia

Proyecto académico desarrollado con fines educativos.

---
