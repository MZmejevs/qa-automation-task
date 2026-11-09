import pytest
from apis.posts import PostsApi


@pytest.mark.full
@pytest.mark.negative
@pytest.mark.xfail(reason="JSONPlaceholder accepts invalid payloads with 201", raises=AssertionError)
def test_post_create_new_post_wrong_type():
    # Send API request to create a new post with wrong value type
    payload = {
        "title": "Automation title Created",
        "body": "Automation body Created",
        "userId": "wrong type"
    }
    response = PostsApi().create_new_post(payload)

    assert 400 <= response.status_code < 500, \
        f"Expected 4xx for missing title, got {response.status_code}"
