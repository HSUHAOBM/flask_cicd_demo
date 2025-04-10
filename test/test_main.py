from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Ian!" in response.data


def test_echo():
    client = app.test_client()
    response = client.post("/api/echo", json={"message": "Hi"})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hi"}


def test_add():
    client = app.test_client()
    response = client.get("/api/add/5/7")
    assert response.status_code == 200
    assert response.get_json() == {"result": 12}
