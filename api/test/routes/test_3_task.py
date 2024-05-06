from fastapi.testclient import TestClient

from api.main import app
from api.src.database.seeds import tasks, users
from api.test.routes.test_2_user import token

client = TestClient(app)

base_url = 'api/v1'

def test_create_task():
    response = client.post(
        f"{base_url}/task/create",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=(tasks[0])
    )
    assert response.status_code == 201

def test_get_all_tasks():
    response = client.get(
        f"{base_url}/task/get_all",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )
    assert response.status_code == 200

def test_update_task():
    response = client.put(
        f"{base_url}/task/update/{1}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json=(tasks[0])
    )
    print(response.json())
    assert response.status_code == 200