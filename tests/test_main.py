from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, world"}


def test_read_item():
    r = client.get("/items/3")
    assert r.status_code == 200
    assert r.json()["item_id"] == 3
