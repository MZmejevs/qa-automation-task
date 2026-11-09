from apis.base_client import BaseClient


class PostsApi(BaseClient):
    def get_all_posts(self):
        """GET /posts
        Get all posts
        :return: requests.Response
        """
        return self.api_request("GET", "/posts")

    def create_new_post(self, data):
        """POST /posts
        Create a new post
        :param data: CreatePostModel
        :return: created post dict
        """
        return self.api_request("POST", "/posts", json=data)

    def update_post(self, post_id: int, data):
        """PUT /posts/{id}
        Update a post
        :param post_id: int
        :param data: UpdatePostModel dict
        :return: PostModel dict
        """
        return self.api_request("PUT", f"/posts/{post_id}", json=data)

    def partial_update_post(self, post_id: int, data):
        """PATCH /posts/{id}
        Partially update a post
        :param post_id: int
        :param data: UpdatePostModel dict
        :return: PostModel dict
        """
        return self.api_request("PATCH", f"/posts/{post_id}", json=data)

    def delete_post(self, post_id: int):
        """DELETE /posts/{id}
        Delete a post
        :param post_id: post_id
        """
        return self.api_request("DELETE", f"/posts/{post_id}")
