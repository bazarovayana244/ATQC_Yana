from users_happy_pass import UserAPI

class TestUserAPI:

    def test_get_users_happy_pass(self):
        response = UserAPI.get_users()
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0

    def test_post_user_happy_pass(self):
        payload = {"name": "Charlie", "age": 28}
        response = UserAPI.create_user(payload)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["user"]["name"] == "Charlie"
        assert data["user"]["age"] == 28

    def test_put_user_happy_pass(self):
        user_id = 3
        payload = {"age": 29}
        response = UserAPI.update_user(user_id, payload)
        assert response.status_code == 200
        data = response.json()
        assert data["age"] == 29

    def test_delete_user_happy_flow(self):
        user_id = 3
        response = UserAPI.delete_user(user_id)
        assert response.status_code == 200
        data = response.json()
        assert data["deleted"]["name"] == "Charlie"
