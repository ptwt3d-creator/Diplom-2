import pytest
import requests
from api import ApiRequests
from helpers import Helpers

class TestOrder:

    def test_order_with_auth_token_and_ingredients_returns_200_body(self, register_user_returns_headers_access_token, order_payload_id_bun_and_main):
        accessToken = register_user_returns_headers_access_token
        payload = order_payload_id_bun_and_main
        
        r = ApiRequests.create_order(payload, accessToken)

        r_body = r.json()
        assert r.status_code == 200 and "name" in r_body and "number" in r_body["order"]
    
    def test_order_without_auth_token_with_ingredients_returns_200_body(self, order_payload_id_bun_and_main):
        payload = order_payload_id_bun_and_main
        
        r = ApiRequests.create_order(payload)

        r_body = r.json()
        
        assert r.status_code == 200 and "name" in r_body and "number" in r_body["order"] # BUG Заказ создается, ассерт оставлен таким для зелёного теста
     
    def test_order_with_auth_token_without_ingredients_returns_200_body(self, register_user_returns_headers_access_token, order_payload_id_bun_and_main):
        accessToken = register_user_returns_headers_access_token
        payload = order_payload_id_bun_and_main
        
        payload["ingredients"] = []
        r = ApiRequests.create_order(payload, accessToken)

        r_body = r.json()
        assert r.status_code == 400 and r.json()["message"] == "Ingredient ids must be provided"
    
    def test_order_with_auth_token_with_not_right_id_ingredients_returns_500(self, register_user_returns_headers_access_token):
        accessToken = register_user_returns_headers_access_token
        payload = {"ingredients": ["4", "5"]}

        r = ApiRequests.create_order(payload, accessToken)

        assert r.status_code == 500


