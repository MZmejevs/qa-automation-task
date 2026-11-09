from apis.base_client import BaseClient

class CommentsApi(BaseClient):
    def get_post_comments(self, post_id):
        """GET /posts/{id}/comments
        Get comments for a specific post
        :param post_id: int
        :return: list of CommentModel dicts
        """
        return self.api_request("GET", f"/posts/{post_id}/comments")
