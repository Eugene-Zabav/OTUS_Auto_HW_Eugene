import pytest
import requests


def test_get_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.parametrize(
    "methods",
    [
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ],
    ids=[
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    ],
)
def test_get_all_breeds_by_invalid_methods(methods):
    response = requests.request(methods, url="https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 405
    assert response.reason == "Method Not Allowed"


@pytest.mark.parametrize(
    ("endpoint", "photos_count"),
    [
        (0, 1),
        (1, 1),
        (15, 15),
        (50, 50),
        (51, 50),
    ],
    ids=[
        "min",
        "min+1",
        "average",
        "max",
        "max+1",
    ],
)
def test_get_random_breeds_by_count(endpoint, photos_count):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{endpoint}")
    assert len(response.json()["message"]) == photos_count


@pytest.mark.parametrize(
    "breed",
    [
        "african",
        "basenji",
        "cavapoo",
    ],
    ids=[
        "african",
        "basenji",
        "cavapoo",
    ],
)
def test_get_random_photo_by_breed(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    assert response.json()["message"].startswith(f"https://images.dog.ceo/breeds/{breed}/")


def test_get_random_breeds():
    response_1 = requests.get("https://dog.ceo/api/breeds/image/random")
    response_2 = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response_1.status_code == response_2.status_code == 200
    assert response_1.json()["message"] != response_2.json()["message"]
