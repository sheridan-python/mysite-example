def test_index(client):
    response = client.get('/banana')
    assert response.status_code == 200
