#!/usr/bin/env python3
"""
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password
    """
    passwd = password.encode('utf-8')
    return bcrypt.hashpw(passwd, bcrypt.gensalt())
