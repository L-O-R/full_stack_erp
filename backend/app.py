from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
)
import sqlite3
from werkzeug.security import check_password_hash
from datetime import timedelta


app = Flask(__name__)

# access given to all
CORS(app)

# setup up the jwt
app.config["JWT_SECRET_KEY"] = "your screte key here"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)

jwt = JWTManager(app)


def get_db_connection():
    conn = sqlite3.connect("nexgen_erg.db")
    conn.row_factory = sqlite3.Row # THis  lets u access columns by name
    return conn


@app.route('/api/login', methods= ['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    user = conn.execute('Select * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()

    if user and check_password_hash(user['password'], password):
        identity = {"username": user['username'], "is_superuser": bool(user['is_superuser'])}
        access_token = create_access_token(identity = identity)
        refresh_token = create_refresh_token(identity = identity)

        return jsonify({
                "access_token" : access_token,
                "refresh_token": refresh_token,
                "user": identity
            }), 200
    return jsonify({"status": "error", "message": "Invalid Credentials"}), 401


@app.route('/api/refresh', methods = ['POST'])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token = access_token)



@app.route('/api/logout', methods = ['POST'])
@jwt_required()
def logout():
    return jsonify({"message": "Successfull logged out"}), 200


if __name__ == "__main__":
    app.run(debug = True, port = 5000)