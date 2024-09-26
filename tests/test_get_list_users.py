import requests
from schemas.get_list_users import list_users
from tests.conftest import base_url
from jsonschema import validate


def test_list_users(base_url):
    url = base_url + '/api/users?page=2'
    params = {"page": 2, "per_page": 6}
    response = requests.get(url, params=params)
    validate(response.json(), schema=list_users)


def test_data_objects_is_equal_per_page_param(base_url):
    url = base_url + '/api/users?page=2'
    per_page = 4
    params = {"page": 2, "per_page": per_page}
    response = requests.get(url, params=params)
    assert len(response.json()['data']) == per_page


def test_all_users_on_page_is_unique(base_url):
    url = base_url + '/api/users?page=2'
    per_page = 4
    params = {"page": 2, "per_page": per_page}
    response = requests.get(url, params=params)
    ids = []
    for i in response.json()['data']:
        ids.append(i['id'])
    assert len(set(ids)) == per_page
