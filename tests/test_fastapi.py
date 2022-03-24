

from app.main import app
from fastapi.testclient import TestClient
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []
