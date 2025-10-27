import requests

BASE_URL = "http://127.0.0.1:5000"
AUTH_TOKEN = "my_secure_token_123"
HEADERS = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": "application/json"}

class UserAPI:
    @staticmethod
    def get_users():
        return requests.get(f"{BASE_URL}/users", headers=HEADERS)

    @staticmethod
    def create_user(user_data):
        return requests.post(f"{BASE_URL}/users", json=user_data, headers=HEADERS)

    @staticmethod
    def update_user(user_id, new_data):
        return requests.put(f"{BASE_URL}/users/{user_id}", json=new_data, headers=HEADERS)

    @staticmethod
    def delete_user(user_id):
        return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
