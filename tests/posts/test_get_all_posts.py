import pytest
from models.posts import PostModel
from apis.posts import PostsApi


@pytest.mark.smoke
@pytest.mark.full
def test_get_all_posts():
    # Send API request to retrieve all posts
    posts = PostsApi().get_all_posts().json()

    assert posts, "No posts returned"

    # Validate returned posts data against the model
    for post in posts:
        PostModel.model_validate(post)
