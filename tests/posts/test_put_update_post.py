import pytest
import pytest_check as check
from models.posts import PostModel, UpdatePostModel
from apis.posts import PostsApi


@pytest.mark.smoke
@pytest.mark.full
def test_put_update_post():
    # Send API request to update post
    post_id = 1
    data = UpdatePostModel(
        id = post_id,
        title = "Automation title Updated",
        body = "Automation body Updated",
        userId= 69
    )
    updated_post = PostsApi().update_post(post_id, data.model_dump()).json()
    assert updated_post, "No post returned after updating"

    # Validate updated post data against the model
    PostModel.model_validate(updated_post)

    # Validate that new post data values are matching
    check.equal(updated_post["id"], data.id, "id doesn't match")
    check.equal(updated_post["title"], data.title, "title doesn't match")
    check.equal(updated_post["body"], data.body, "body doesn't match")
    check.equal(updated_post["userId"], data.userId, "userId doesn't match")
