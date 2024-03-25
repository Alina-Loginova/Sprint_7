import requests
import allure

from urls import LOGIN

@allure.suite('Авторизация курьера')
class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_login_courier(self, register_new_courier):
        payload = {
            "login": register_new_courier['login_pass']['login'],
            "password": register_new_courier['login_pass']['password']
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Авторизация курьера без логина')
    def test_login_without_login(self, register_new_courier):
        payload = {
            "password": register_new_courier['login_pass']['password']
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 400 and response.json().get('message')== "Недостаточно данных для входа"

    @allure.title('Авторизация несуществующего курьера')
    def test_login_non_existent_courier(self, register_new_courier):
        payload = {
            "login": register_new_courier['login_pass']['login'] + '1',
            "password": register_new_courier['login_pass']['password']
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message')== "Учетная запись не найдена"

    @allure.title('Авторизация с невалидным паролем курьера')
    def test_login_courier_with_invalid_password(self, register_new_courier):
        payload = {
            "login": register_new_courier['login_pass']['login'],
            "password": register_new_courier['login_pass']['password'] + '1'
        }
        response = requests.post(LOGIN, data=payload)
        assert response.status_code == 404 and response.json().get('message')== "Учетная запись не найдена"