

class TestUrl:

    REGISTER_USER = "https://stellarburgers.education-services.ru/api/auth/register"
    
    LOGIN = "https://stellarburgers.education-services.ru/api/auth/login"
    
    CREATE_ORDER = "https://stellarburgers.education-services.ru/api/orders"
    
    GET_INGREDIENTS = "https://stellarburgers.education-services.ru/api/ingredients"

    DELETE_USER = "https://stellarburgers.education-services.ru/api/auth/user"

class TestData:

    ORDER_PAYLOAD_ID_BUN_AND_MAIN = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
    
    ORDER_PAYLOAD_NOT_RIGHT_ID_BUN_AND_MAIN = {"ingredients": ["4", "5"]}