import pytest
import requests


@pytest.mark.parametrize(
    "brewer_id",
    [
        "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
        "5128df48-79fc-4f0f-8b52-d06be54d0cec",
    ],
    ids=[
        "id #1",
        "id #2",
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
        (0, 0),
        (1, 1),
        (100, 100),
        (200, 200),
        (201, 200),
    ],
    ids=[
        "min",
        "1",
        "average",
        "max",
        "max+1",
    ],
)
def test_get_specified_breweries_count(endpoint, breweries_count):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?per_page={endpoint}")
    assert response.status_code == 200
    assert len(response.json()) == breweries_count


@pytest.mark.parametrize(
    ("url_city", "response_city"),
    [
        ("san_diego", "San Diego"),
        ("austin", "Austin"),
    ],
    ids=[
        "San Diego",
        "Austin",
    ],
)
def test_get_breweries_by_city(url_city, response_city):
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={url_city}&per_page=3")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["city"] == response_city


def test_breweries_metadata():
    response = requests.get("https://api.openbrewerydb.org/v1/breweries/meta")
    assert list(response.json().keys()) == [
        "total",
        "page",
        "per_page",
    ]
