import requests
import pytest


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


def test_get_status_code_by_url(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code
