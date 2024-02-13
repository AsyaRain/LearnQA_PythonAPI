import requests
import pytest

base_url = "https://playground.learnqa.ru/api/user/"


def test_edit_user_unauthorized():
    user_id = 2  # ID пользователя, данные которого мы пытаемся изменить
    data = {"firstName": "John"}  # Новые данные пользователя
    response = requests.put(base_url + str(user_id), data=data)
    assert response.status_code == 401, f"Unexpected status code: {response.status_code}"


def test_edit_user_authorized_different_user():
    auth_data = {"email": "vinkotov@example.com", "password": "1234"}
    response_auth = requests.post(base_url + "login", data=auth_data)
    assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
    auth_token = response_auth.json()["token"]

    user_id = 3  # ID другого пользователя, данные которого мы пытаемся изменить
    data = {"firstName": "John"}  # Новые данные пользователя
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.put(base_url + str(user_id), headers=headers, data=data)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"


def test_edit_user_invalid_email():
    auth_data = {"email": "vinkotov@example.com", "password": "1234"}
    response_auth = requests.post(base_url + "login", data=auth_data)
    assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
    auth_token = response_auth.json()["token"]

    user_id = 2  # ID того же пользователя, данные которого мы пытаемся изменить
    data = {"email": "invalid_email.com"}  # Новый email пользователя без символа @
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.put(base_url + str(user_id), headers=headers, data=data)
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}"


def test_edit_user_short_first_name():
    auth_data = {"email": "vinkotov@example.com", "password": "1234"}
    response_auth = requests.post(base_url + "login", data=auth_data)
    assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
    auth_token = response_auth.json()["token"]

    user_id = 2  # ID того же пользователя, данные которого мы пытаемся изменить
    data = {"firstName": "J"}  # Очень короткое значение для firstName (в один символ)
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.put(base_url + str(user_id), headers=headers, data=data)
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
