from users_happy_pass import UserAPI

class TestUserAPI:
    def test_user_management_happy_flow(self):
        #GET
        response = UserAPI.get_users()
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) > 0

        #POST
        payload = {"name": "Charlie", "age": 28}
        response = UserAPI.create_user(payload)
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        user_id = data["id"]
        assert data["user"]["name"] == "Charlie"
        assert data["user"]["age"] == 28

        #PUT
        update_payload = {"age": 29}
        response = UserAPI.update_user(user_id, update_payload)
        assert response.status_code == 200
        data = response.json()
        assert data["age"] == 29

        #DELETE
        response = UserAPI.delete_user(user_id)
        assert response.status_code == 200
        data = response.json()
        assert data["deleted"]["name"] == "Charlie"
