import pytest
from .conftest import client


def test_get_author():
    response = client.get("/bs/v1/author/1")
    data = response.json()
    assert response.status_code == 200