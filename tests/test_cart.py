def test_add_to_cart(client):
    response = client.post("/cart/add", json={"product_id": 1, "quantity": 2})
    assert response.status_code == 200

    data = response.get_json()
    assert any(item["id"] == 1 for item in data)


def test_remove_from_cart(client):
    # Primero agregamos
    client.post("/cart/add", json={"product_id": 2, "quantity": 1})

    # Luego eliminamos
    response = client.delete("/cart/2")
    assert response.status_code == 200

    data = response.get_json()
    assert all(item["id"] != 2 for item in data)


def test_cart_total(client):
    # Limpiar agregando un item y eliminando
    client.post("/cart/add", json={"product_id": 1, "quantity": 1})

    response = client.get("/cart/total")
    assert response.status_code == 200

    data = response.get_json()
    assert "total" in data
    assert data["total"] >= 0
