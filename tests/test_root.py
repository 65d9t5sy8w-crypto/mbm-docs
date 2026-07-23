from fastapi.testclient import TestClient

from mbm.api.main import app


def test_root() -> None:
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["service"] == "mbm-api"
