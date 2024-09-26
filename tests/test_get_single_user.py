import requests
from schemas.get_single_user import single_user
from tests.conftest import base_url
from jsonschema import validate


def test_get_single_user(base_url):
    url = base_url + '/api/users/4'
    response = requests.get(url)
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=single_user)


def test_method_return_only_one_user(base_url):
    url = base_url + '/api/users/4'
    response = requests.get(url)
    body = response.json()
    ids_count = 0
    for i in body['data']:
        if i == 'id':
            ids_count += 1
    assert ids_count == 1


def test_id_in_url_equal_id_from_response(base_url):
    id_in_url = 5
    url = base_url + f'/api/users/{id_in_url}'
    response = requests.get(url)
    body = response.json()
    id_from_response = body['data']['id']
    assert id_in_url == id_from_response
