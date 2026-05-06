from flask import Blueprint, jsonify

cart_bp = Blueprint("cart", __name__)

@cart_bp.get("/")
def cart_root():
    return jsonify({"message": "Cart endpoint OK"}), 200
