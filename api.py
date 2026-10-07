import requests
from data import TestUrl
import allure


class ApiRequests:
    
    def get_list_ingredients():
        return requests.get(TestUrl.GET_INGREDIENTS)

    def create_order(payload, headers=None):
        return requests.post(TestUrl.CREATE_ORDER, payload, headers=headers)

    def login(payload):    
        return requests.post(TestUrl.LOGIN, payload)

    def register_user(payload):
        return requests.post(TestUrl.REGISTER_USER, payload)

    def get_ingredients():
        return requests.post(TestUrl.GET_INGREDIENTS)

    def delete_user(token):
        headers = {"Authorization": token}
        return requests.post(TestUrl.DELETE_USER, headers=headers)
