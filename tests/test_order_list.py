import allure
import requests

from urls import ORDERS

@allure.suite('Список заказов')
class TestOrderList:
    @allure.title('Проверка метода списка заказов')
    def test_oder_list(self):
        response = requests.get(ORDERS)
        assert response.status_code == 200 and 'orders' in response.json()
        assert type(response.json()['orders']) is list