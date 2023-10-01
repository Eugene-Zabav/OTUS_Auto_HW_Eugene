import pytest
import requests


@pytest.mark.parametrize(
    ("endpoint", "items_count"),
    [
        ("posts", 100),
        ("comments", 500),
        ("albums", 100),
        ("photos", 5000),
        ("todos", 200),
        ("users", 10),
    ],
    ids=[
        "posts",
        "comments",
        "albums",
        "photos",
        "todos",
        "users",
    ],
)
def test_get_max_items_for_endpoints(endpoint, items_count):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{endpoint}")
    assert response.status_code == 200
    assert len(response.json()) == items_count


@pytest.mark.parametrize(
    "post_id",
    [
        1,
        2,
    ],
    ids=[
        "id #1",
        "id #2",
    ],
)
def test_post_by_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_breweries_metadata():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert list(response.json().keys()) == [
        "userId",
        "id",
        "title",
        "body",
    ]


def test_response_body_of_get_comments_by_post_and_search_comments_by_post_are_equal():
    get_comments_by_post = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    search_comments_by_post = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    assert get_comments_by_post.status_code == search_comments_by_post.status_code == 200
    assert get_comments_by_post.text == search_comments_by_post.text


@pytest.mark.parametrize(
    "post_id",
    [
        1,
        2,
    ],
    ids=[
        "id #1",
        "id #2",
    ],
)
def test_get_comments_by_post_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    for comment in response.json():
        assert comment["postId"] == post_id
