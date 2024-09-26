import requests
from schemas.put_update import update
from tests.conftest import base_url
from jsonschema import validate


def test_update(base_url):
    url = base_url + '/api/users/2'
    user_data = {"name": "Antoni", "job": "Project manager"}
    response = requests.put(url, json=user_data)
    validate(response.json(), schema=update)


def test_user_data_equal_updated_data(base_url):
    url = base_url + '/api/users/2'
    user_data = {"name": "Antoni", "job": "Project manager"}
    response = requests.put(url, json=user_data)
    assert response.json()['name'] == user_data['name']
    assert response.json()['job'] == user_data['job']


def test_name_field_is_not_required(base_url):
    url = base_url + '/api/users/2'
    user_data = {"job": "Project manager"}
    response = requests.put(url, json=user_data)
    validate(response.json(), schema=update)
