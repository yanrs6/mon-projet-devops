from app import app


def test_home_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_title():
    client = app.test_client()
    response = client.get("/")
    assert b"Mon premier projet DEVOPS !" in response.data


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

