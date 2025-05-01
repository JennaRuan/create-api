import pytest
from flask import json

from app.main import app
from app.models import Task, db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
    with app.app_context():
        db.drop_all()


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "status": "pending",
        },
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["title"] == "Test Task"
