import pytest
import requests
from api import ApiRequests
from helpers import Helpers

class TestLogin:

    def test_login_registered_user_returns_200_body_accessToken_refreshToken(self, register_user):
        reg_data = register_user

        payload = {
            "email": reg_data["email"],
            "password": reg_data["password"]
        }

        r = ApiRequests.login(payload)

        r_body = r.json()
        assert r.status_code == 200 and "accessToken" in r_body and "refreshToken" in r_body

    @pytest.mark.parametrize(
        "name_test, not_right_field",
        [
        ("Логином", {"email": "testnotrightemail836@yandex.ru"}),
        ("Паролем", {"password": "testnotpassword836"}),
        ("Логином и паролем (не существующий пользователь)", {"email": "testnotrightemail896@yandex.ru", "password": "testnotpassword896"}),
        ]
    )
    def test_login_registered_user_with_not_right_data_returns_401_message(self, name_test, not_right_field, register_user):
        reg_data = register_user

        payload = {
            "email": reg_data["email"],
            "password": reg_data["password"]
        }
        payload.update(not_right_field)

        r = ApiRequests.login(payload)

        assert r.status_code == 401 and r.json()["message"] == "email or password are incorrect"
    