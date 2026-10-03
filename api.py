import requests
from data import TestUrl
import allure


class ApiRequests:
    
    def get_list_ingredients():
        return requests.get(TestUrl.GET_INGREDIENTS)

    def create_order(payload):
        return requests.post(TestUrl.CREATE_ORDER, payload)

    def login(payload):    
        return requests.post(TestUrl.LOGIN, payload)

    def register_user(payload):
        return requests.post(TestUrl.REGISTER_USER, payload)


