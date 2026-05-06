from flask import Blueprint, jsonify
from controllers.products_controller import get_all_products

products_bp = Blueprint("products", __name__)

@products_bp.get("/")
def list_products():
    """
    Endpoint real para obtener todos los productos.
    """
    products, error = get_all_products()

    if error:
        return jsonify({"error": error}), 500

    return jsonify(products), 200
