#!/usr/bin/env python3
"""
"""
from auth import Auth
from flask import Flask, jsonify, request, abort


app = Flask(__name__)
AUTH = Auth()


@app.route('/', strict_slashes=False)
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """implements /users route
    """
    email = request.form["email"]
    password = request.form["password"]
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """implements login
    """
    email = request.form["email"]
    password = request.form["password"]
    if AUTH.valid_login(email, password):
       session_id =  AUTH.create_session(email)
       resp = jsonify({"email": email, "message": "logged in"})
       resp.set_cookie("session_id", session_id)
       return resp
    else:
       abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
