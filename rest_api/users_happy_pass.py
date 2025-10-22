import requests

BASE_URL = "http://127.0.0.1:5000"
HEADERS = {"Authorization": "Bearer my_secure_token_123", "Content-Type": "application/json"}

def test_get_users_happy_pass():
    response = requests.get(f"{BASE_URL}/users", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0

def test_post_user_happy_pass():
    payload = {"name": "Charlie", "age": 28}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["user"]["name"] == "Charlie"
    assert data["user"]["age"] == 28

def test_put_user_happy_pass():
    payload = {"age": 29}
    user_id = 3
    response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["age"] == 29

def test_delete_user_happy_flow():
    user_id = 3
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["deleted"]["name"] == "Charlie"
