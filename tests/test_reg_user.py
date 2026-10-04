import pytest
import allure
import requests
from api import ApiRequests
from helpers import Helpers


@allure.suite("API Пользователи")
@allure.sub_suite("Регистрация нового пользователя")
class TestRegisterUser:

    @allure.title("Успешная регистрация уникального пользователя")
    @allure.description("Проверка создания нового аккаунта с генерацией уникальных данных, получение статус-кода 200 и токенов")
    def test_register_new_unic_user_returns_200_body_accessToken_refreshToken(self):
        payload = Helpers.generate_payload_registration()

        r = ApiRequests.register_user(payload)

        r_body = r.json()
        assert r.status_code == 200 and "accessToken" in r_body and "refreshToken" in r_body

    @allure.title("Попытка регистрации уже существующего пользователя")
    @allure.description("Проверка возвращения кода 403 и сообщения о дубликате при попытке создать юзера с занятым email")
    def test_register_user_with_taken_login_returns_403_message(self):
        payload = Helpers.generate_payload_registration()
        payload1 = Helpers.generate_payload_registration()
        
        payload1.update({
            "email": payload["email"]
            })

        ApiRequests.register_user(payload)
        r = ApiRequests.register_user(payload1)
 
        assert r.status_code == 403 and r.json()["message"] == "User already exists"

    @allure.title("Регистрация пользователя без обязательного поля")
    @allure.description("Параметризованный тест для проверки ошибки 403 при попытке зарегистрироваться без логина, пароля или имени")  
    @pytest.mark.parametrize(
        "name_test, missing_field",
        [
        ("Логина", {"email": ""}),
        ("Пароля",{"password": ""}),
        ("Имени",{"name": ""})
        ]
    )
    def test_register_new_user_without_required_field_returns_403_message(self, name_test, missing_field):
        payload = Helpers.generate_payload_registration()
        
        payload.update(missing_field) 
        r = ApiRequests.register_user(payload)

        r_body = r.json()
        assert r.status_code == 403 and r.json()["message"] == "Email, password and name are required fields"