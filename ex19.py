import requests
import pytest
import allure

base_url = "https://playground.learnqa.ru/api/user/"
login_url = base_url + "login"


class TestUserDelete:

    @allure.feature("Delete User")
    @allure.story("Unauthorized attempt to delete user")
    def test_delete_user_unauthorized(self):
        user_id = 2
        data = {"email": "vinkotov@example.com", "password": "1234"}
        response_auth = requests.post(login_url, data=data)
        assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
        auth_token = response_auth.json()["token"]
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.delete(base_url + str(user_id), headers=headers)
        assert response.status_code == 400, f"Unexpected status code: {response.status_code}"

    @allure.feature("Delete User")
    @allure.story("Positive delete user scenario")
    def test_delete_user_positive(self):
        # Создаем нового пользователя
        data = {"email": "test@example.com", "password": "password"}
        response_create = requests.post(base_url, data=data)
        assert response_create.status_code == 201, f"Failed to create user with status code {response_create.status_code}"
        user_id = response_create.json()["id"]

        # Авторизуемся под созданным пользователем и удаляем его
        auth_data = {"email": "test@example.com", "password": "password"}
        response_auth = requests.post(login_url, data=auth_data)
        assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
        auth_token = response_auth.json()["token"]
        headers = {"Authorization": f"Bearer {auth_token}"}
        response_delete = requests.delete(base_url + str(user_id), headers=headers)
        assert response_delete.status_code == 200, f"Failed to delete user with status code {response_delete.status_code}"

        # Попытка получить данные удаленного пользователя
        response_get_deleted_user = requests.get(base_url + str(user_id))
        assert response_get_deleted_user.status_code == 404, f"Deleted user still exists with status code {response_get_deleted_user.status_code}"

    @allure.feature("Delete User")
    @allure.story("Unauthorized attempt to delete user by another user")
    def test_delete_user_authorized_different_user(self):
        user_id = 2  # ID другого пользователя, которого мы пытаемся удалить
        data = {"email": "another_user@example.com", "password": "password"}
        response_auth = requests.post(login_url, data=data)
        assert response_auth.status_code == 200, f"Failed to log in with status code {response_auth.status_code}"
        auth_token = response_auth.json()["token"]
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.delete(base_url + str(user_id), headers=headers)
        assert response.status_code == 400, f"Unexpected status code: {response.status_code}"
