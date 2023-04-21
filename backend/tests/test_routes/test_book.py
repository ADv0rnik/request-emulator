import json

def test_get_book(client):    
    response = client.get("/books/1")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data['title'] == 'Hobbit'


def test_get_books(client):
    response = client.get("/books/")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)


