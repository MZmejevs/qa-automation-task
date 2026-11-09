import pytest
import pytest_check as check
from models.posts import PostModel, CreatePostModel
from apis.posts import PostsApi


@pytest.mark.smoke
@pytest.mark.full
def test_post_create_new_post():
    # Send API request to create new post
    data = CreatePostModel(
        title = "Automation title Created",
        body = "Automation body Created",
        userId= 69
    )
    new_post = PostsApi().create_new_post(data.model_dump()).json()
    assert new_post, "No post returned after creating new post"

    # Validate created post data against the model
    PostModel.model_validate(new_post)

    # Validate that new post data values are matching
    check.equal(new_post["title"], data.title, "title doesn't match")
    check.equal(new_post["body"], data.body, "body doesn't match")
    check.equal(new_post["userId"], data.userId, "userId doesn't match")
