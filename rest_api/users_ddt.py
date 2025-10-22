import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
AUTH_TOKEN = "my_secure_token_123"
HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": "application/json"}

#new users
create_user_data = [
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28},
    {"name": "Eve", "age": 35},
]

#update users
update_user_data = [
    {"name": "Charlie Updated", "age": 23},
    {"name": "Diana Updated", "age": 29},
    {"name": "Eve Updated", "age": 36},
]

# GET
def test_get_users():
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, dict)
    # Перевіряємо, що хоча б один користувач є
    assert len(users) > 0

# POST
@pytest.mark.parametrize("user_data", create_user_data)
def test_create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data, headers=HEADERS)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["user"]["name"] == user_data["name"]
    assert response_data["user"]["age"] == user_data["age"]
    assert "id" in response_data

# PUT
@pytest.mark.parametrize("user_id,new_data", [(1, update_user_data[0]), (2, update_user_data[1])])
def test_update_user(user_id, new_data):
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=new_data, headers=HEADERS)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["name"] == new_data["name"]
    assert updated_user["age"] == new_data["age"]

# DELETE
@pytest.mark.parametrize("user_id", [1, 2])
def test_delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    deleted_data = response.json()
    assert "deleted" in deleted_data
