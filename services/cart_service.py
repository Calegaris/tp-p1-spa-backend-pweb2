from data.memory_store import cart
from services.products_service import load_products

def add_item(product_id, quantity):
    """
    Agrega un producto al carrito.
    Si ya existe, suma la cantidad.
    """
    products = load_products()
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return None, "Producto no encontrado"

    # Buscar si ya está en el carrito
    existing = next((item for item in cart if item["id"] == product_id), None)

    if existing:
        existing["quantity"] += quantity
    else:
        cart.append({
            "id": product_id,
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

    return cart, None


def remove_item(product_id):
    """
    Elimina un producto del carrito.
    """
    global cart
    before = len(cart)
    cart = [item for item in cart if item["id"] != product_id]

    if len(cart) == before:
        return None, "El producto no está en el carrito"

    return cart, None


def calculate_total():
    """
    Calcula el total del carrito.
    """
    total = sum(item["price"] * item["quantity"] for item in cart)
    return total
