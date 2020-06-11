from fastapi.testclient import TestClient
from main import app
from json import loads
from app.schemas.user import UserSchema
import uuid

client = TestClient(app)


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert loads(response.text) != None


def test_get_user():
    response = client.get("/users/1555fda6-f66b-4aea-93a9-f9646f5c5b5b")
    assert response.status_code == 404


def test_create_user():
    response = client.post("/users/", json={
        "id": str(uuid.uuid4()),
        "email": f"{str(uuid.uuid4())}@test.com",
        "is_active": "True",
    })
    assert response.status_code == 201
