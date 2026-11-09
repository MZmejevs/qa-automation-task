import pytest
from apis.posts import PostsApi


@pytest.mark.full
@pytest.mark.negative
@pytest.mark.xfail(reason="JSONPlaceholder accepts invalid payloads with 201", raises=AssertionError)
def test_post_create_new_post_missing_value():
    # Send API request to create a new post with missing title value
    payload = {
        # missing title value
        "body": "Automation body MZ",
        "userId": 1
    }
    response = PostsApi().create_new_post(payload)

    assert 400 <= response.status_code < 500, \
        f"Expected 4xx for missing title, got {response.status_code}"
