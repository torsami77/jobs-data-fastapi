from fastapi.testclient import TestClient

from api.main import app
from api.src.database.seeds import tasks, users
from api.test.routes.test_3_user import token

client = TestClient(app)

base_url = 'api/v1'


def test_get_all_products():
    response = client.get(
        f"{base_url}/product/get_all",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )
    assert response.status_code == 200
