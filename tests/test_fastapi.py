from sqlalchemy.orm import sessionmaker
import pytest

from app.main import app
from app.database import Base, engine, get_db
from fastapi.testclient import TestClient
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    # Dependency override

    def override_get_db():
        try:

            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


@pytest.mark.parametrize("success_path, success_code", [
    ("/", 200),
    ("/posts", 200)
])
def test_read_main(client, success_path, success_code):
    response = client.get(success_path)
    assert response.status_code == success_code
