import pytest
import pytest_check as check
from apis.posts import PostsApi


@pytest.mark.smoke
@pytest.mark.full
def test_delete_post_by_id():
    # Send API request to delete post by id
    post_id = 67
    response = PostsApi().delete_post(post_id)

    # Validate that the post was deleted successfully
    assert response.status_code == 200, \
        f"Expected 200 for post id {post_id}, got {response.status_code}"

    # Validate that the body is empty
    check.equal(response.json(), {}, f"Expected empty body, got {response.json()}")
