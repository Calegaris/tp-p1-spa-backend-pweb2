# Controlador de productos
from services.products_service import load_products

def get_all_products():
    """
    Controlador que obtiene todos los productos.
    No tiene lógica de negocio, solo coordina el servicio.
    """
    try:
        products = load_products()
        return products, None  # (data, error)
    except Exception as e:
        return None, str(e)
