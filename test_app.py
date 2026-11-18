import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_release_allowed_when_tests_pass(client):
    response = client.get("/release-check/0")
    assert response.status_code == 200
    assert response.get_json() == {"failed_tests": 0, "can_release": True}


def test_release_blocked_when_a_test_fails(client):
    response = client.get("/release-check/1")
    assert response.status_code == 200
    assert response.get_json() == {"failed_tests": 1, "can_release": False}


def test_negative_count_is_rejected(client):
    assert client.get("/release-check/-1").status_code == 404


def test_non_numeric_count_is_rejected(client):
    assert client.get("/release-check/many").status_code == 404
