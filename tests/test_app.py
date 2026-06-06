import pytest
from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "CI Demo API is running"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add(client):
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_subtract(client):
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.get_json()["result"] == 6


def test_multiply(client):
    response = client.post("/multiply", json={"a": 6, "b": 7})
    assert response.status_code == 200
    assert response.get_json()["result"] == 42


def test_divide(client):
    response = client.post("/divide", json={"a": 8, "b": 2})
    assert response.status_code == 200
    assert response.get_json()["result"] == 4


def test_divide_by_zero(client):
    response = client.post("/divide", json={"a": 8, "b": 0})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Division by zero is not allowed"


def test_invalid_payload(client):
    response = client.post("/add", json={"a": "x", "b": 2})
    assert response.status_code == 400
