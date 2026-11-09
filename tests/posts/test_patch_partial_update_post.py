import pytest
import pytest_check as check
from models.posts import PostModel, UpdatePostModel
from apis.posts import PostsApi


@pytest.mark.full
def test_patch_partial_update_post():
    # Send API request to partially update post
    post_id = 1
    data = UpdatePostModel(
        title = "Automation title Created",
    )
    updated_post = PostsApi().partial_update_post(post_id, data.model_dump(exclude_unset=True)).json()

    assert updated_post, "No post returned after partially updating post"

    # Validate partially updated post data against the model
    PostModel.model_validate(updated_post)

    # Validate that partially updated post data values are matching
    check.equal(updated_post["id"], post_id, "id doesn't match")
    check.equal(updated_post["title"], data.title, "title doesn't match")
