import requests
import pytest

base_url = "https://playground.learnqa.ru/api/user/"


@pytest.mark.parametrize("email", ["invalid_email.com", "noat.com"])
def test_create_user_invalid_email(email):
    data = {"email": email, "password": "password"}
    response = requests.post(base_url, data=data)
    assert response.status_code == 400

@pytest.mark.parametrize("missing_param", ["email", "password"])
def test_create_user_missing_field(missing_param):
    data = {"email": "test@example.com", "password": "password"}
    del data[missing_param]
    response = requests.post(base_url, data=data)
    assert response.status_code == 400


def test_create_user_short_name():
    data = {"email": "test@example.com", "password": "password", "username": "a"}
    response = requests.post(base_url, data=data)
    assert response.status_code == 400


def test_create_user_long_name():
    data = {"email": "test@example.com", "password": "password", "username": "a" * 251}
    response = requests.post(base_url, data=data)
    assert response.status_code == 400
