import pytest
import requests
from api import ApiRequests
from helpers import Helpers


class TestRegisterUser:

    def test_register_new_unic_user_returns_200_body_accessToken_refreshToken(self):
        payload = Helpers.generate_payload_registration()

        r = ApiRequests.register_user(payload)

        r_body = r.json()
        assert r.status_code == 200 and "accessToken" in r_body and "refreshToken" in r_body

    def test_register_user_with_taken_login_returns_403_message(self):
        payload = Helpers.generate_payload_registration()
        payload1 = Helpers.generate_payload_registration()
        
        payload1.update({
            "email": payload["email"]
            })

        ApiRequests.register_user(payload)
        r = ApiRequests.register_user(payload1)
 
        assert r.status_code == 403 and r.json()["message"] == "User already exists"

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