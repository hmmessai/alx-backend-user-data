#!/usr/bin/env python3
"""Defines BasicAuth class
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Represents BasicAuth
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extracts the base64 authorization header
        """
        if authorization_header and type(authorization_header) == str:
            auth_scheme = authorization_header.split(' ')
            if auth_scheme[0] == 'Basic':
                return auth_scheme[1]
            return None
        return None
