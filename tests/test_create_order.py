import allure
import requests
import pytest

from urls import ORDERS


@allure.suite('Создание заказа')
class TestCreateOrder:
    @allure.title('Успешное создание заказа')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], None])
    def test_create_order(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        response = requests.post(ORDERS, json=payload)
        assert response.status_code == 201 and 'track' in response.text