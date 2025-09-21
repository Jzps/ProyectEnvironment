"""
Módulo que centraliza las exportaciones de los tipos de autos.

Este archivo reexporta las clases de autos disponibles para que
puedan importarse directamente desde el paquete `autos`.

Clases exportadas:
    AutoNuevo
    AutoUsado
    AutoElectrico
"""

from .tipos import AutoNuevo, AutoUsado, AutoElectrico

__all__ = ["AutoNuevo", "AutoUsado", "AutoElectrico"]
