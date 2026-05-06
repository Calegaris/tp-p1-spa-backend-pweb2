from flask import Blueprint, request, jsonify
from controllers.cart_controller import add_to_cart, remove_from_cart, get_cart_total

cart_bp = Blueprint("cart", __name__)

@cart_bp.post("/add")
def add_product():
    data = request.get_json()

    if not data or "product_id" not in data or "quantity" not in data:
        return jsonify({"error": "Faltan parámetros: product_id y quantity"}), 400

    product_id = data["product_id"]
    quantity = data["quantity"]

    cart, error = add_to_cart(product_id, quantity)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(cart), 200


@cart_bp.delete("/<int:product_id>")
def delete_product(product_id):
    cart, error = remove_from_cart(product_id)

    if error:
        return jsonify({"error": error}), 400

    return jsonify(cart), 200


@cart_bp.get("/total")
def cart_total():
    total = get_cart_total()
    return jsonify({"total": total}), 200
