#!/usr/bin/env python3
"""Defines SessionExpAuth class
"""
from os import getenv
from datetime import datetime
from api.v1.auth.session_exp_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Representation of SessionExpAuth
    """
    def __init__(self):
        """Initializes instance of SessionExpAuth
        """
        self.session_duration = 0
        duration = getenv('SESSION_DURATION')
        if duration and int(duration):
            self.session_duration = int(duration)

    def create_session(self, user_id=None):
        """Creates a session
        """
        session_id = super().create_session(user_id)
        if session_id:
            session_dictionary = {}
            session_dictionary['user_id'] = user_id
            session_dictionary['created_at'] = datetime.now()
            self.user_id_by_session_id[session_id] = sesion_dictionary
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Get the user_id for the given session_id
        """
        user_session = self.user_id_by_session_id
        if session_id or session_id in user_session:
            if self.session_duration <= 0:
                return user_session[session_id]['user_id']
            createdAt = user_session[session_id]['created_at']
            if createdAt:
                if createdAt.timedelta():
                    return user_session[session_id]['user_id']
