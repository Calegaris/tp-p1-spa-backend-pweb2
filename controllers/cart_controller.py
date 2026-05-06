from services.cart_service import add_item, remove_item, calculate_total

def add_to_cart(product_id, quantity):
    cart, error = add_item(product_id, quantity)
    return cart, error

def remove_from_cart(product_id):
    cart, error = remove_item(product_id)
    return cart, error

def get_cart_total():
    total = calculate_total()
    return total
