from starlette.testclient import TestClient
from api.app import create_app
from api.config import settings
client = TestClient(create_app(settings))

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
