import pytest
from users_ddt import UserAPI

create_user_data = [
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 28},
    {"name": "Eve", "age": 35},
]

update_user_data = [
    {"name": "Charlie Updated", "age": 23},
    {"name": "Diana Updated", "age": 29},
    {"name": "Eve Updated", "age": 36},
]

class TestUserAPI:

    def test_get_users(self):
        response = UserAPI.get_users()
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, dict)
        assert len(users) > 0

    @pytest.mark.parametrize("user_data", create_user_data)
    def test_create_user(self, user_data):
        response = UserAPI.create_user(user_data)
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["user"]["name"] == user_data["name"]
        assert response_data["user"]["age"] == user_data["age"]
        assert "id" in response_data

    @pytest.mark.parametrize("user_id,new_data", [(1, update_user_data[0]), (2, update_user_data[1])])
    def test_update_user(self, user_id, new_data):
        response = UserAPI.update_user(user_id, new_data)
        assert response.status_code == 200
        updated_user = response.json()
        assert updated_user["name"] == new_data["name"]
        assert updated_user["age"] == new_data["age"]

    @pytest.mark.parametrize("user_id", [1, 2])
    def test_delete_user(self, user_id):
        response = UserAPI.delete_user(user_id)
        assert response.status_code == 200
        deleted_data = response.json()
        assert "deleted" in deleted_data
