from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []


class TestClass:

    def test_one(self):
        print('test_one')
        x = "this"
        assert "h" in x

    def test_two(self):
        print('test_two')
        x = "hello"
        assert x == "hello"
