from tests.utils import generate_book_id


def test_get_book(client):
    response = client.get(f"/books/{generate_book_id()}")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, dict)


def test_get_books(client):
    response = client.get("/books/")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)


