import random
import string

class Helpers:
    
    @staticmethod
    def generate_random_string(length=10):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    @staticmethod
    def generate_payload_registration(length=10):
        return {
            "email": Helpers.generate_random_string(length) + "@yandex.ru",
            "password": Helpers.generate_random_string(length),
            "name": Helpers.generate_random_string(length)
        }

    