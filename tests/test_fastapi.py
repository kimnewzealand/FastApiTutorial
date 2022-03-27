import pytest

from app.main import app
from fastapi.testclient import TestClient
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

client = TestClient(app)


@pytest.mark.parametrize("success_path, success_code", [
    ("/", 200),
    ("/posts", 200)
])
def test_read_main(success_path, success_code):
    response = client.get(success_path)
    assert response.status_code == success_code
