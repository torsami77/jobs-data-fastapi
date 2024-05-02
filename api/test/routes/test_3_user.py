from fastapi.testclient import TestClient

from api.main import app
from api.src.database.seeds import users, tasks

client = TestClient(app)

base_url = 'api/v1'

# def test_sign_up_user():
#     response = client.post(
#         f"{base_url}/sign_up_user", 
#         data=(users[0])
#         )
#     assert response.status_code == 201

def auth_user():
    return client.post(
        f"{base_url}/token",
        data=(users[1])
    )
response = auth_user()

def test_token():
    assert response.status_code == 200
    assert type(response.json()['access_token']) == str
    assert type(response.json()['role']) == str
    token = response.json()['access_token']

token = response.json()['access_token']