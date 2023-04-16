import pytest


def test_get_author(client):
    response = client.get("/author/1")
    data = response.json()
    assert response.status_code == 200
    assert data['first_name'] == 'John'
    assert data['last_name'] == 'Tolkien'