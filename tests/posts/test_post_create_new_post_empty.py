import pytest
from apis.posts import PostsApi


@pytest.mark.full
@pytest.mark.negative
@pytest.mark.xfail(reason="JSONPlaceholder accepts invalid payloads with 201", raises=AssertionError)
def test_create_post_with_empty_payload():
    # Send API request to create a new post with empty payload
    response = PostsApi().create_new_post({})

    assert 400 <= response.status_code < 500, f"Expected 4xx, got {response.status_code}"
