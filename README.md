# ¡¡¡¡¡IMPORTANTE!!!!!

Para que el sistema funcione correctamente tienes dos opciones:

1. **Reiniciar la base de datos local**  
   - Si estás trabajando con SQLite, simplemente elimina el archivo `autos.db`.  
   - Al ejecutar el programa nuevamente, se recrearán las tablas automáticamente.

2. **Iniciar sesión con el usuario administrador por defecto**  
   - **USUARIO:** Usuario  
   - **CONTRASEÑA:** 123  

```markdown
# 🚗 Concesionario de Autos en Python

Este proyecto es un **sistema de gestión para un concesionario de autos**, desarrollado en **Python** con **SQLAlchemy** y **PostgreSQL** (Neon DB).  
Permite **registrar, vender, dar mantenimiento y administrar autos, clientes, empleados, facturas y mantenimientos** de forma estructurada.


---

## 📂 Estructura del Proyecto

```

ProyectEnvironment/
│── autos/                   # Clases que representan los distintos tipos de autos
│   ├── base.py              # Clase base Auto
│   ├── tipos.py             # Subclases: AutoNuevo, AutoUsado, AutoElectrico
│
│── crud/                    # Operaciones CRUD directas sobre la base de datos
│   ├── admin\_crud.py        # CRUD de administradores
│   ├── auto\_crud.py         # CRUD de autos
│   ├── cliente\_crud.py      # CRUD de clientes
│   ├── concesionario\_crud.py# CRUD del concesionario
│   ├── empleado\_crud.py     # CRUD de empleados
│   ├── especialidad\_crud.py # CRUD de especialidades de técnicos
│   ├── factura\_crud.py      # CRUD de facturas
│   ├── mantenimiento\_crud.py# CRUD de mantenimientos
│
│── database/                # Configuración y entidades de la base de datos
│   ├── base.py              # Base declarativa de SQLAlchemy
│   ├── config.py            # Configuración de conexión (Postgres/Neon)
│   ├── db.py                # Sesiones y motor de base de datos
│   ├── init\_db.py           # Inicialización de tablas
│   └── entities/            # Definición de modelos (tablas)
│
│── schemas/                 # Esquemas con Pydantic (validación de datos)
│   ├── admin\_schema.py
│   ├── auto\_schema.py
│   ├── cliente\_schema.py
│   ├── concesionario\_schema.py
│   ├── empleado\_schema.py
│   ├── especialidad\_schema.py
│   ├── factura\_schema.py
│   ├── mantenimiento\_schema.py
│
│── services/                # Lógica de negocio (intermediarios entre CRUD y main)
│   ├── admin\_service.py     # Servicio para login de administradores
│   ├── cliente\_service.py   # Gestión de clientes
│   ├── concesionario\_service.py # Operaciones principales del concesionario
│   ├── empleado\_service.py  # Gestión de empleados
│   ├── factura\_service.py   # Generación automática de facturas al vender autos
│   ├── mantenimiento\_service.py # Registro de mantenimientos
│
│── main.py                  # Menú principal (punto de entrada al sistema)
│── reset\_db.py              # Script opcional para reiniciar las tablas
│── test\_connection.py       # Script para probar conexión con la base de datos
│── requirements.txt         # Dependencias necesarias
│── README.md                # Este archivo

````

---

## ⚙️ Requisitos Previos

- **Python 3.10+**
- **PostgreSQL** (se usa NeonDB en la nube)
- Librerías listadas en `requirements.txt`

Instala las dependencias con:

```bash
pip install -r requirements.txt
````

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**

```bash
git clone https://github.com/Jzps/ProyectEnvironment.git
cd ProyectEnvironment
```

2. **Configurar la base de datos:**

El proyecto está preparado para **NeonDB (Postgres en la nube)**.
Debes configurar la variable `DATABASE_URL` en `database/config.py` con tu conexión a Neon o Postgres local.

Ejemplo:

```python
DATABASE_URL = "postgresql+psycopg2://usuario:contraseña@host/dbname"
```

3. **Inicializar la base de datos:**

```bash
python init_db.py
```

4. **Ejecutar el programa:**

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

* **Concesionario (Autos):** Comprar, vender, mostrar autos, registrar mantenimientos y listar autos vendidos.
* **Clientes:** Registrar, listar y eliminar clientes.
* **Empleados:** Registrar empleados, vendedores y técnicos de mantenimiento.
* **Mantenimientos:** Listar mantenimientos realizados.
* **Salir:** Termina el programa.

---

## 📝 Descripción de la Lógica

* **Autos:**
  Representados por clases (`AutoNuevo`, `AutoUsado`, `AutoElectrico`), guardados en BD vía `auto_crud`.

* **Clientes y Empleados:**
  Gestión completa con validación de datos (`cliente_service`, `empleado_service`).

* **Ventas:**
  Al vender un auto se marca como vendido y se **genera automáticamente una factura** con datos del cliente, vendedor y auto.

* **Mantenimientos:**
  Se asigna un técnico y se guarda el detalle y costo en la tabla correspondiente.

---

## 💡 Ideas Futuras

* Reportes en PDF de facturas.
* Interfaz gráfica o API REST con FastAPI.
* Autenticación avanzada de usuarios (más de un rol).

---

## 👨‍💻 Autores

* Juan Pablo Gutiérrez Vargas
* Juan Felipe Ospina Agudelo

---

## 📜 Licencia

Este proyecto puede ser usado y modificado con fines **educativos y personales**.

```

---