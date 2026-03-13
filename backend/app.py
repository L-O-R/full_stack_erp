from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# access given to all
CORS(app)

USER_CREDENTIALS = {
    "admin":{"username": "admin", "password": "1234", "role": "admin"},
}

@app.route('/api/login', methods= ['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username]['password'] == password:
        return jsonify({
            "status": "success",
            "user": {"username": username, "role": USER_CREDENTIALS[username]['role']}

        }), 200
    return jsonify({"status": "error", "message": "Invalid Credentials"}), 401



if __name__ == "__main__":
    app.run(debug = True, port = 5000)