#!/usr/bin/env python3
"""Defines SessionAuth class
"""
from models.user import User
from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Represents instances of SessionAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session
        """
        if user_id and type(user_id) == str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets the user from the given session_id
        """
        if session_id and type(session_id) == str:
            for sid in self.user_id_by_session_id.keys():
                if session_id == sid:
                    return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """Gets the current user
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        if user_id:
            user = User.get(user_id)
            return user

    def destroy_session(self, request=None):
        """Deletes the user session when logging out
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
