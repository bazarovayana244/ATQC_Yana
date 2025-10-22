from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

AUTH_TOKEN = "my_secure_token_123"

# AUTHORIZATION
def check_auth():
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {AUTH_TOKEN}":
        return False
    return True

# GET
@app.route("/users", methods=["GET"])
def get_users():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(users), 200

# POST
@app.route("/users", methods=["POST"])
def create_user():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# PUT
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

# DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"deleted": deleted_user}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

