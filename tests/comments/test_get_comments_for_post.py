import pytest
import pytest_check as check
from models.comments import CommentModel
from apis.comments import CommentsApi


@pytest.mark.full
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_comments(post_id):
    # Send API request to comments for a specific post
    post_id = 1
    comments = CommentsApi().get_post_comments(post_id).json()

    assert comments, f"No comments returned for post with id: {post_id}"

    # Validate returned comments
    for item in comments:
        CommentModel.model_validate(item)

        # Validate that the returned comments has the correct post id
        check.equal(item["postId"], post_id, f"Expected post id {post_id}, got {item['id']}")
