#!/usr/bin/env python3
"""Defines Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Representation of Auth instance/object
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if the path requires authentication
        """
        if path == None or excluded_paths == None or excluded_paths == []: 
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User
        """
        return None
