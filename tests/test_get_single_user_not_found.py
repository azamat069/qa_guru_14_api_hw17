import requests
from tests.conftest import base_url


def test_get_single_user_not_found(base_url):
    url = base_url + '/api/users/23'
    response = requests.get(url)
    assert response.status_code == 404


def test_json_is_empty(base_url):
    url = base_url + '/api/users/23'
    response = requests.get(url)
    assert len(response.json()) == 0
