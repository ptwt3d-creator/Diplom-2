import pytest
import requests
from helpers import Helpers
from api import ApiRequests

@pytest.fixture
def register_user():
    payload = Helpers.generate_payload_registration()
    
    ApiRequests.register_user(payload)

    return payload
