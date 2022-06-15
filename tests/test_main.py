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

    yield client


def cleanup():
    db.drop_all()


def test_index_not_logged_in(client):
    response = client.get("/")
    assert b'Enter your username' in response.data


def test_index_logged_in(client):
    client.post("/login", data={"user-username": "borp", "user-password": "geslo"}, follow_redirects=True)
    response = client.get("/")
    assert b'Enter your message' in response.data


def test_all_routes(client):
    client.post("/login", data={"user-username": "borp", "user-password": "geslo"}, follow_redirects=True)
    all_pages = ["/", "/profile", "/users"]
    for page in all_pages:
        response = client.get(page)
        assert response.status_code is 200
