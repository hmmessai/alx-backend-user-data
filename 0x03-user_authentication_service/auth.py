#!/usr/bin/env python3
"""Defines User authentication and Auth clas
"""
from sqlalchemy.exc import NoResultFound
from user import User
from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password
    """
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user
        raise ValueError('User {} already exists.'.format(email))
