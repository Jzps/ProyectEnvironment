from database.config import SessionLocal
from crud import mantenimiento_crud, factura_crud, auto_crud
from schemas.factura_schema import FacturaCreate
from uuid import UUID


class FacturaService:
    """
    Servicio para gestionar facturas de autos.

    Permite crear facturas, listar todas las facturas registradas y eliminarlas.
    Calcula automáticamente el total considerando mantenimientos y descuentos.
    """

    def __init__(self, db=None):
        """
        Inicializa el servicio de facturas con una sesión de base de datos.

        Args:
            db: Sesión de SQLAlchemy (opcional). Si no se proporciona, se crea una nueva.
        """

        self.db = db or SessionLocal()

    def crear_factura(self, factura: FacturaCreate, usuario_id: UUID | None = None):
        """
        Crea una factura para un auto vendido y calcula automáticamente
        el costo de mantenimientos y el total.

        Args:
            factura (FacturaCreate): Datos de la factura a crear.
            usuario_id (UUID | None): ID del usuario que realiza la creación.

        Returns:
            Factura creada o None si el auto no existe o no está vendido.
        """

        auto = auto_crud.obtener_auto_por_id(self.db, factura.auto_id)
        if not auto or not auto.vendido:
            print("El auto no existe o no está vendido.")
            return None

        mantenimientos = mantenimiento_crud.obtener_mantenimientos_por_auto(
            self.db, factura.auto_id
        )
        costo_mantenimiento_total = sum(m.costo for m in mantenimientos)

        factura.total = (
            factura.precio_carro_base + costo_mantenimiento_total - factura.descuento
        )
        factura.costo_mantenimiento = costo_mantenimiento_total

        return factura_crud.crear_factura(self.db, factura, usuario_id)

    def listar_facturas(self):
        """
        Obtiene la lista de todas las facturas registradas.

        Returns:
            list: Lista de facturas.
        """

        return factura_crud.obtener_facturas(self.db)

    def eliminar_factura(self, factura_id: UUID):
        """
        Elimina una factura por su ID.

        Args:
            factura_id (UUID): ID de la factura a eliminar.

        Returns:
            Factura eliminada o None si no existe.
        """
        
        return factura_crud.eliminar_factura(self.db, factura_id)
