def test_get_products(client):
    response = client.get("/products/")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    # Validar estructura mínima
    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "price" in first
