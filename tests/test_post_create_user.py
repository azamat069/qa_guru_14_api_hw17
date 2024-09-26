import requests
from jsonschema.exceptions import ValidationError
from schemas.post_create_user import create_user
from tests.conftest import base_url
from jsonschema import validate


def test_create_user(base_url):
    url = base_url + '/api/users'
    name = "Justin"
    job = "QA"
    json_data = {"name": name, "job": job}
    response = requests.post(url, json=json_data)
    validate(response.json(), schema=create_user)
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.status_code == 201


def test_registered_users_have_different_ids(base_url):
    url = base_url + '/api/users'
    user_data_1 = {
        "name": "Justin",
        "job": "QA"
    }
    user_data_2 = {
        "name": "Bob",
        "job": "Developer"
    }
    response_first_user = requests.post(url, json=user_data_1)
    response_second_user = requests.post(url, json=user_data_2)
    assert response_first_user.json()['id'] != response_second_user.json()['id']


def test_additional_fields_not_accepted(base_url):
    url = base_url + '/api/users'
    name = "Johnatan"
    job = "Analitics"
    hobbies = "football"
    json_data = {"name": name, "job": job, "hobbies": hobbies}
    response = requests.post(url, json=json_data)
    try:
        validate(response.json(), schema=create_user)
        assert False, 'Валидация с полем hobbies прошла успешно, но это не должно было произойти'
    except ValidationError:
        print('Валидация не прошла, это ожидаемый результат')


def test_name_field_is_required(base_url):
    url = base_url + '/api/users'
    job = "Analitics"
    json_data = {"job": job}
    response = requests.post(url, json=json_data)
    try:
        validate(response.json(), schema=create_user)
        assert False, 'Валидация без поля name прошла успешно, но это не должно было произойти'
    except ValidationError:
        print('Валидация не прошла, это ожидаемый результат')
