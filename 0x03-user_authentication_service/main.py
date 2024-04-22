#!/usr/bin/env python3
"""
Main file
"""
import requests


URL = 'http://0.0.0.0:5000/'


def register_user(email: str, password: str) -> None:
    """testing register_user route by sending requests with
    the requests module"""
    data = {'email': email, 'password': password}
    post_req = requests.post(URL + 'users', data=data)
    assert post_req.json() == {'email': email,
                               'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """testing login route by sending requests
    with the requests module"""
    data = {'email': email, 'password': password}
    post_req = requests.post(URL + 'sessions', data=data)
    assert post_req.status_code == 401


def profile_unlogged() -> None:
    """testing profile route by sending requests
    with the requests module"""
    get_req = requests.get(URL + 'profile')
    assert get_req.status_code == 403


def log_in(email: str, password: str) -> str:
    """testing login endpoint by sending requests
    with the requests module"""
    data = {'email': email, 'password': password}
    post_req = requests.post(URL + 'sessions', data=data)
    session_id = post_req.cookies.get('session_id')
    assert post_req.json() == {"email": email,
                               "message": "logged in"}
    return session_id


def profile_logged(session_id: str) -> None:
    """testing profile endpoint by sending requests
    with the requests module"""
    session_cookie = {'session_id': session_id}
    get_req = requests.get(URL + 'profile', cookies=session_cookie)
    assert get_req.status_code == 200


def log_out(session_id: str) -> None:
    """testing logout endpoint by sending requests
    with the requests module"""
    session_cookie = {'session_id': session_id}
    delete_req = requests.delete(URL + 'sessions',
                                 cookies=session_cookie)
    assert delete_req.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """testing reset_password endpoint by sending requests
    with the requests module"""
    data = {'email': email}
    post_req = requests.post(URL + 'reset_password',
                             data=data)
    assert post_req.status_code == 200
    return post_req.json()['reset_token']


def update_password(email: str,
                    reset_token: str, new_password: str) -> None:
    """testing reset_password endpoint by sending requests
    with the requests module"""
    data = {
        'email': email,
        'new_password': new_password,
        'reset_token': reset_token
    }

    put_req = requests.put(URL + 'reset_password',
                           data=data)
    assert put_req.status_code == 200
    assert put_req.json() == {'email': email,
                              'message': 'Password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
