import requests
import pytest

base_url = "https://playground.learnqa.ru/api/user/"
login_url = base_url + "login"


@pytest.fixture
def get_auth_token():
    data = {"email": "vinkotov@example.com", "password": "1234"}
    response = requests.post(login_url, data=data)
    assert response.status_code == 200, f"Failed to log in with status code {response.status_code}"
    response_data = response.json()
    if "token" not in response_data:
        raise Exception("Token is missing in the response")
    auth_token = response_data["token"]
    return auth_token


def test_get_other_user_data(get_auth_token):
    auth_token = get_auth_token
    headers = {"Authorization": f"Bearer {auth_token}"}
    user_id = 3  # ID другого пользователя, данные которого мы хотим запросить
    response = requests.get(base_url + str(user_id), headers=headers)
    assert response.status_code == 200, f"Failed to get user data with status code {response.status_code}"
    user_data = response.json()
    assert "username" in user_data, "Username is not present in user data"
    assert "email" not in user_data, "Email should not be present in user data"
    assert "password" not in user_data, "Password should not be present in user data"
