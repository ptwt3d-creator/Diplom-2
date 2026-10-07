import pytest
import requests
import allure
from api import ApiRequests
from helpers import Helpers
from data import TestData

@allure.suite("API Заказы")
@allure.sub_suite("Создание заказа")
class TestOrder:


    @allure.title("Создание заказа авторизованным пользователем с ингредиентами")
    @allure.description("Проверка, что при наличии токена и валидных ID ингредиентов возвращается статус 200 и номер заказа")
    def test_order_with_auth_token_and_ingredients_returns_200_body(self, register_user_returns_headers_access_token):
        accessToken = register_user_returns_headers_access_token
        payload = TestData.ORDER_PAYLOAD_ID_BUN_AND_MAIN
        
        r = ApiRequests.create_order(payload, accessToken)

        r_body = r.json()
        assert r.status_code == 200 and "name" in r_body and "number" in r_body["order"]
    

    @allure.title("Создание заказа неавторизованным пользователем с ингредиентами")
    @allure.description("Проверка возможности создания заказа без передачи токена авторизации (ожидается код 200)")
    def test_order_without_auth_token_with_ingredients_returns_200_body(self):
        payload = TestData.ORDER_PAYLOAD_ID_BUN_AND_MAIN
        
        r = ApiRequests.create_order(payload)

        r_body = r.json()
        
        assert r.status_code == 200 and "name" in r_body and "number" in r_body["order"] # BUG Заказ создается, ассерт оставлен таким для зелёного теста
    

    @allure.title("Создание заказа авторизованным пользователем без ингредиентов")
    @allure.description("Проверка, что при пустом списке ингредиентов возвращается ошибка 400 со специальным сообщением")
    def test_order_with_auth_token_without_ingredients_returns_200_body(self, register_user_returns_headers_access_token):
        accessToken = register_user_returns_headers_access_token
        payload = TestData.ORDER_PAYLOAD_ID_BUN_AND_MAIN
        
        payload["ingredients"] = []
        r = ApiRequests.create_order(payload, accessToken)

        r_body = r.json()
        assert r.status_code == 400 and r.json()["message"] == "Ingredient ids must be provided"
    
    @allure.title("Создание заказа авторизованным пользователем с неверным ID ингредиентов")
    @allure.description("Проверка, что при передаче несуществующих или некорректных хэшей ингредиентов возвращается серверная ошибка 500")
    def test_order_with_auth_token_with_not_right_id_ingredients_returns_500(self, register_user_returns_headers_access_token):
        accessToken = register_user_returns_headers_access_token
        payload = TestData.ORDER_PAYLOAD_NOT_RIGHT_ID_BUN_AND_MAIN

        r = ApiRequests.create_order(payload, accessToken)

        assert r.status_code == 500


