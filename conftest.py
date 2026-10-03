import pytest
import requests
from helpers import Helpers
from api import ApiRequests

@pytest.fixture
def register_user_returns_body_with_all_reg_data():
    payload = Helpers.generate_payload_registration()
    
    r = ApiRequests.register_user(payload)
    reg_data = r.json()

    #Добавили данные регистарции в корень тела ответа
    reg_data.update(payload)
    return reg_data

@pytest.fixture
def register_user_returns_headers_access_token():
    payload = Helpers.generate_payload_registration()
    
    r = ApiRequests.register_user(payload)

    return {"accessToken": r.json()["accessToken"]}

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
def order_payload_id_bun_and_main():
    return {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}

@pytest.fixture
def order_payload_not_right_id_bun_and_main():
    return {"ingredients": ["111115a71d1f82001bdaaa6d", "111115a71d1f82001bdaaa6f"]}

