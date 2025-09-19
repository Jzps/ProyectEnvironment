# ¡¡¡¡¡IMPORTANTE!!!!!

Para que el sistema funcione correctamente:

  **Iniciar sesión con el usuario administrador por defecto**  
   - **USUARIO:** Usuario  
   - **CONTRASEÑA:** 123  

---

# 🚗 Concesionario de Autos en Python

Este proyecto es un **sistema de gestión para un concesionario de autos**, desarrollado en **Python** con **SQLAlchemy** y **PostgreSQL (NeonDB)**.

Permite **registrar, vender, dar mantenimiento y administrar autos, clientes, empleados, facturas y mantenimientos** de forma estructurada.

---

## 📂 Estructura del Proyecto

```bash
ProyectEnvironment/
│── autos/                   # Clases que representan los distintos tipos de autos
│   ├── base.py              # Clase base Auto
│   ├── tipos.py             # Subclases: AutoNuevo, AutoUsado, AutoElectrico
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
│── main.py                  # Menú principal (punto de entrada al sistema)
│── reset_db.py              # Script opcional para reiniciar las tablas
│── test_connection.py       # Script para probar conexión con la base de datos
│── requirements.txt         # Dependencias necesarias
│── README.md                # Documentación del proyecto
```

---

## ⚙️ Requisitos Previos

* **Python 3.10+**
* **PostgreSQL** (se recomienda NeonDB en la nube)
* Librerías listadas en `requirements.txt`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/Jzps/ProyectEnvironment.git
cd ProyectEnvironment
```

2. **Configurar la base de datos**

En el archivo `.env` debes definir tu conexión a Neon o Postgres local. Ejemplo:

```env
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@host/dbname
```

3. **Inicializar la base de datos**

```bash
python database/init_db.py
```

4. **Probar la conexión (opcional)**

```bash
python test_connection.py
```

5. **Ejecutar el programa**

```bash
python main.py
```

---

## 📖 Uso del Sistema

### Menú Principal

```text
=== MENÚ PRINCIPAL ===
1. Concesionario (Autos)
2. Clientes
3. Empleados
4. Mantenimientos
5. Salir
```

🔹 **Concesionario (Autos):** Comprar, vender, mostrar autos, registrar mantenimientos y listar autos vendidos.
🔹 **Clientes:** Registrar, listar y eliminar clientes.
🔹 **Empleados:** Registrar empleados, vendedores y técnicos de mantenimiento.
🔹 **Mantenimientos:** Listar mantenimientos realizados.
🔹 **Salir:** Termina el programa.

---

## 📝 Lógica de Negocio

* **Autos:**
  Representados por clases (`AutoNuevo`, `AutoUsado`, `AutoElectrico`), guardados en BD vía `auto_crud`.

* **Clientes y Empleados:**
  Gestión completa con validación de datos (`cliente_service`, `empleado_service`).

* **Ventas:**
  Al vender un auto se marca como vendido y se **genera automáticamente una factura** con datos del cliente, vendedor y auto.

* **Mantenimientos:**
  Se asigna un técnico y se guarda el detalle y costo en la tabla correspondiente.

* **Login de Administradores:**
  El sistema incluye un **módulo de login** que permite validar credenciales antes de usar el sistema.

---

## 👨‍💻 Autores

* Juan Pablo Gutiérrez Vargas
* Juan Felipe Ospina Agudelo

---

## 📜 Licencia

Este proyecto puede ser usado y modificado con fines **educativos y personales**.

---