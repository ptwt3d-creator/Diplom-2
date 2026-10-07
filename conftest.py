import pytest
import requests
from helpers import Helpers
from api import ApiRequests

@pytest.fixture
def register_user_returns_body_with_all_reg_data_cleanup_yield():
    payload = Helpers.generate_payload_registration()
    
    r = ApiRequests.register_user(payload)
    reg_data = r.json()

    # Забрали токен из ответ, для последующего удаления созданного пользователя
    token = reg_data["accessToken"]

    # Чтобы брать данные использованные при регистрации(логин, пароль, имя) в тестах при необходимости, добавили их в корень тела ответа
    reg_data.update(payload)
    
    yield reg_data
    
    ApiRequests.delete_user(token) # Удаление пользователя после теста

@pytest.fixture
def register_user_returns_headers_access_token_cleanup_yield():
    payload = Helpers.generate_payload_registration()
    
    r = ApiRequests.register_user(payload)
    token = r.json()["accessToken"]
    
    yield {"accessToken": token}

    ApiRequests.delete_user(token) # Удаление пользователя после теста


@pytest.fixture
def login_user_returns_login_body(register_user):
    reg_data = register_user
    
    payload = {
        "email": reg_data["email"],
        "password": reg_data["password"]
    }

    ApiRequests.login(payload)
    
    login_data = r.json()
    return login_data

@pytest.fixture
def cleanup_user_after_test():
    tokens_to_clean = []

    # Отдаем в тест лямбду, которая принимает список токенов в tokens_list и переносит его в tokens_to_clean с помощью extend
    yield lambda tokens_list: tokens_to_clean.extend(tokens_list)

    for token in tokens_to_clean:
        if token != "":
            ApiRequests.delete_user(token)