#!/usr/bin/env python3
"""Defines BasicAuth class
"""
from models.user import User
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
import re


class BasicAuth(Auth):
    """Represents BasicAuth
    """
    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """Extracts the base64 authorization header
        """
        if authorization_header and type(authorization_header) == str:
            auth_scheme = authorization_header.split(' ')
            if auth_scheme[0] == 'Basic':
                return auth_scheme[1]
            return None
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Decodes the base64 authorization header
        """
        b64_auth_head = base64_authorization_header
        if b64_auth_head and type(b64_auth_head) == str:
            try:
                decoded_value = base64.b64decode(b64_auth_head)
                decoded_value = decoded_value.decode('utf-8')
            except Exception:
                return None
            return decoded_value
        return None

    def extract_user_credentials(self,
                                 decode_base64_authorization_header: str
                                 ) -> (str, str):
        """Extracts user email and password from decoded value
        """
        dcd_b64_auth_head = decode_base64_authorization_header
        if dcd_b64_auth_head and type(dcd_b64_auth_head) == str:
            if ':' in dcd_b64_auth_head:
                credentials = dcd_b64_auth_head.split(':')
                user_email = credentials[0]
                user_pwd = credentials[1]
                return (user_email, user_pwd)
            return (None, None)
        return (None, None)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Provides User from the enterd credentials
        """
        if user_email and user_pwd and\
           type(user_email) == str and type(user_pwd) == str:
            user = User.search({'email': user_email})
            if user:
                if user[0].is_valid_password(user_pwd):
                    return user[0]
                return None
            return None
        return None
