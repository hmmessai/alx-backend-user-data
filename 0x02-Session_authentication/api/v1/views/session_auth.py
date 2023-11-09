#!/usr/bin/env python3
"""View for the app related to session_auth
"""
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Login operation
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if not email:
        return jsonify({'error': "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth

    session_id = auth.create_session(user[0].id)
    user_repr = jsonify(user[0].to_json())
    cookie = getenv('SESSION_NAME')
    user_repr.set_cookie(cookie, session_id)

    return user_repr


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Logout operation
    """
    from api.v1.app import auth
    status = auth.destroy_session(request)
    if status is False:
        abort(404)
    return jsonify({}), 200
