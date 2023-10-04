import pytest
import requests


@pytest.mark.parametrize(
    "brewer_id",
    [
        pytest.param("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", id="id #1"),
        pytest.param("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", id="id #2"),
    ],
)
def test_brewer_by_id(brewer_id):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/{brewer_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewer_id


def test_brewer_by_wrong_id():
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries/0")
    assert response.status_code == 404
    assert response.json()["message"] == "Couldn't find Brewery"
    assert response.reason == "Not Found"


@pytest.mark.parametrize(
    ("endpoint", "breweries_count"),
    [
        pytest.param(0, 0, id="min"),
        pytest.param(1, 1, id="min+1"),
        pytest.param(100, 100, id="average"),
        pytest.param(200, 200, id="max"),
        pytest.param(201, 200, id="max+1"),
    ],
)
def test_get_specified_breweries_count(endpoint, breweries_count):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?per_page={endpoint}")
    assert response.status_code == 200
    assert len(response.json()) == breweries_count


@pytest.mark.parametrize(
    ("url_city", "response_city"),
    [
        pytest.param("san_diego", "San Diego", id="San Diego"),
        pytest.param("austin", "Austin", id="Austin"),
    ],
)
def test_get_breweries_by_city(url_city, response_city):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={url_city}&per_page=3")
    assert response.status_code == 200
    assert len(response.json()) == 3
    for brewery in response.json():
        assert brewery["city"] == response_city


def test_breweries_metadata():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")
    assert list(response.json().keys()) == [
        "total",
        "page",
        "per_page",
    ]
