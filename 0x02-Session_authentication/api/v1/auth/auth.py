#!/usr/bin/env python3
"""Defines Auth class
"""
import re
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """Representation of Auth instance/object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if the path requires authentication
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '/':
                    pattern = '{}'.format(exclusion_path[:-1])
                else:
                    pattern = '{}'.format(exclusion_path[0:])
                if re.match(pattern, path) or re.match(path, exclusion_path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request:
            if request.headers.get('Authorization'):
                return request.headers.get('Authorization')
            return None

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        """
        return None

    def session_cookie(self, request=None):
        """Gets the cookie value from a request
        """
        cookie = getenv('SESSION_NAME')
        if request:
            return request.cookies.get(cookie)
        return None
