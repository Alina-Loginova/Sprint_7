import requests
import pytest
from urls import CREATE_COURIER
from helpers import generate_random_string


@pytest.fixture 
def register_new_courier():

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(CREATE_COURIER, data=payload)

    if response.status_code == 201:
        login_pass = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return {'login_pass': login_pass, 'response': response}


@pytest.fixture 
def generate_payload():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield payload