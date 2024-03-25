import requests
import allure

from urls import CREATE_COURIER

@allure.suite('Регистрация курьера')
class TestCreateCourier:
    @allure.title('Успешная регистрация курьера')
    def test_create_new_courier(self, register_new_courier):
        assert register_new_courier['response'].status_code == 201 and register_new_courier['response'].text == '{"ok":true}'
    
    @allure.title('Повторная регистрация курьера')
    def test_create_used_courier(self, register_new_courier):
        payload = {
            "login": register_new_courier['login_pass']['login'],
            "password": register_new_courier['login_pass']['password'],
            "firstName": register_new_courier['login_pass']['password']
        }
        response = requests.post(CREATE_COURIER, data=payload)
        assert response.status_code == 409 and response.json().get('message')== "Этот логин уже используется. Попробуйте другой."

    @allure.title('Регистрация курьера без атрибутов')
    def test_create_courier_without_keys(self):
        response = requests.post(CREATE_COURIER, data={})
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для создания учетной записи"

    @allure.title('Регистрация курьера без логина')
    def test_create_courier_without_login(self, generate_payload):
        payload = generate_payload
        payload['login'] = None
        response = requests.post(CREATE_COURIER, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для создания учетной записи"

    @allure.title('Регистрация курьера без обязательных атрибутов')
    def test_create_courier_with_required_attr(self, generate_payload):
        payload = generate_payload
        del payload['firstName']
        response = requests.post(CREATE_COURIER, data=payload)
        assert response.status_code == 201 and response.text == '{"ok":true}'
