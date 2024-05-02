from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/api/v1", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {"Welcome": "jobs-data-assignment-samson-samuel"}