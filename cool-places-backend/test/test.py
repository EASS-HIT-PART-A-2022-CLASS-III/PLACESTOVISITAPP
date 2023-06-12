

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import sys
from os.path import abspath, dirname

sys.path.append(dirname(dirname(abspath(__file__))))


 
from main import app, get_db
from main import LocationCreate, LocationUpdate

client = TestClient(app)


@pytest.fixture
def db():
    from main import engine, Base
    from sqlalchemy.orm import Session

    # Create a new SQLite in-memory database for testing
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def test_create_location(db: Session):
    # Test the creation of a new location
    response = client.post("/locations", json={"name": "Camp Nou", "country": "Spain", "description": "Barcelona cool football stadium"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Camp Nou"
    assert data["country"] == "Spain"
    assert data["description"] == "Barcelona cool football stadium"


def test_read_location(db: Session):
    # Test the retrieval of a location
    response = client.get("/locations/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    assert data["name"] == "Camp nou"
    assert data["country"] == "Spain"
    assert data["description"] == "Barcelona cool football stadium"


def test_update_location(db: Session):
    # Test the updating of a location
    response = client.put("/locations/1", json={"name": "New Camp Nou", "country": "Spain", "description": "Updated description"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    assert data["name"] == "New Camp Nou"
    assert data["country"] == "Spain"
    assert data["description"] == "Updated description"


def test_delete_location(db: Session):
    # Test the deletion of a location
    response = client.delete("/locations/1")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Location deleted successfully."


