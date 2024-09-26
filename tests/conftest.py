import pytest


@pytest.fixture(scope="function", autouse=True)
def base_url():
    return 'https://reqres.in'
