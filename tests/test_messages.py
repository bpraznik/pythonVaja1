import os
import pytest

from app.database import db

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    cleanup()
    db.create_all()

    client.post("/login", data={"user-username": "borp", "user-password": "geslo"}, follow_redirects=True)

    yield client


def cleanup():
    db.drop_all()


def test_post_message(client):
    client.post("/add-message", data={"text": "Test message"}, follow_redirects=True)
    response = client.get("/")
    assert b'Test message' in response.data
