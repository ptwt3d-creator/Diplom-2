import pytest
import requests
import allure
from api import ApiRequests
from helpers import Helpers


@allure.suite("API Авторизация")
@allure.sub_suite("Логин пользователя")
class TestLogin:

    @allure.title("Успешный логин зарегистрированного пользователя")
    @allure.description("Проверка, что при вводе корректных данных возвращается статус 200 и токены авторизации")
    def test_login_registered_user_returns_200_body_accessToken_refreshToken(self, register_user_returns_body_with_all_reg_data_cleanup_yield):
        reg_data = register_user_returns_body_with_all_reg_data_cleanup_yield

        payload = {
            "email": reg_data["email"],
            "password": reg_data["password"]
        }

        r = ApiRequests.login(payload)

        r_body = r.json()
        assert r.status_code == 200 and "accessToken" in r_body and "refreshToken" in r_body

    @allure.title("Логин пользователя с некорректными данными")
    @allure.description("Параметризованный тест с неверным "+" {name_test} "+" для проверки ошибки 401 при неверном логине, пароле или несуществующем юзере")
    @pytest.mark.parametrize(
        "name_test, not_right_field",
        [
        ("Логином", {"email": "testnotrightemail836@yandex.ru"}),
        ("Паролем", {"password": "testnotpassword836"}),
        ("Логином и паролем (не существующий пользователь)", {"email": "testnotrightemail896@yandex.ru", "password": "testnotpassword896"}),
        ]
    )
    def test_login_registered_user_with_not_right_data_returns_401_message(self, name_test, not_right_field, register_user_returns_body_with_all_reg_data_cleanup_yield):
        reg_data = register_user_returns_body_with_all_reg_data_cleanup_yield

        payload = {
            "email": reg_data["email"],
            "password": reg_data["password"]
        }
        payload.update(not_right_field)

        r = ApiRequests.login(payload)

        assert r.status_code == 401 and r.json()["message"] == "email or password are incorrect"
    