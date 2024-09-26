import requests
from tests.conftest import base_url


def test_delete_user(base_url):
    url = base_url + '/api/users/2'
    response = requests.delete(url)
    assert response.status_code == 204
