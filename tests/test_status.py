from fastapi.testclient import TestClient

from mbm.api.main import app


def test_status() -> None:
    client = TestClient(app)
    response = client.get("/api/status")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["architecture_revision"] == 8
