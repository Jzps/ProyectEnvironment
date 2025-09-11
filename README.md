## Concesionario de Autos en Python

Este proyecto es un sistema de gestión para un concesionario de autos. Está desarrollado en Python y permite **comprar**, **vender**, **mostrar** y **dar mantenimiento** a autos de diferentes tipos: **nuevos**, **usados** y **eléctricos**.

---

## Estructura del Proyecto

concesionario

auto.py # Clase base Auto
tipos_autos.py # Clases específicas: AutoNuevo, AutoUsado, AutoElectrico
concesionario.py # Clase Concesionario que gestiona los autos
main.py # Menú principal (punto de entrada)
README.md # Este archivo
Prueba.txt lugar donde compartir ideas a implementar

---

## Requisitos Previos

- Python 3.8 o superior instalado
- No necesitas instalar librerías adicionales

Puedes verificar la versión de Python ejecutando:

```bash
python --version

---

## Paso 1: Clonar el repositorio

Abre tu terminal y ejecuta el siguiente comando para clonar el proyecto:

git clone https://github.com/Jzps/ProyectEnvironment.git

Reemplaza tu-usuario con tu nombre de usuario en GitHub (si lo subiste allí).

Luego, entra a la carpeta del proyecto:

cd concesionario

## Paso 2: Ejecutar el programa

Desde la carpeta donde está main.py, ejecuta:

python main.py

## Paso 3: Usar el programa

Una vez que el programa se ejecuta, verás este menú en consola:

--- MENÚ CONCESIONARIO ---
1. Comprar Auto
2. Vender Auto
3. Mostrar Autos
4. Dar Mantenimiento
5. Salir

Opciones disponibles:

## Comprar Auto

Seleccionas si es nuevo, usado o eléctrico

Ingresas los datos como marca, modelo, precio, etc.

## Vender Auto

Eliges el auto por índice y se elimina de la lista

## Mostrar Autos

Muestra todos los autos actualmente en el concesionario

## Dar Mantenimiento

Según el tipo de auto, se ofrecen diferentes opciones

Salir

Termina la ejecución del programa

---

## ¿Cómo funciona el código?

Auto: Clase base con atributos comunes a todos los autos

AutoNuevo, AutoUsado, AutoElectrico: Subclases con información y mantenimiento específico

Concesionario: Administra una lista de autos y operaciones sobre ellos

main.py: Contiene el menú interactivo que conecta todo el sistema

---

## Ideas para futuras mejoras

Guardar y cargar autos desde un archivo

Añadir una interfaz gráfica

---

## Licencia

Este proyecto puede ser usado y modificado libremente con fines educativos o personales.

Autores

Desarrollado por:
Juan Pablo Gutierrez Vargas 
Juan Felipe Ospina Agudelo