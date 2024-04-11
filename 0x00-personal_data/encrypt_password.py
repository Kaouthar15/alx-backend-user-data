#!/usr/bin/env python3
"""Defining two function hash_password and is_valid"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a hashed password"""
    b_password = password.encode()
    hashed_pswd = bcrypt.hashpw(b_password, bcrypt.gensalt())
    return hashed_pswd


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validates that the provided password matches
    the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
