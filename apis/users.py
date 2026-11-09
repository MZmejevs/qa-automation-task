from apis.base_client import BaseClient


class UsersApi(BaseClient):
    def get_all_users(self):
        """GET /users
        Get all users
        :return: list of UserModel dict
        """
        return self.api_request("GET", "/users")

    def get_user_by_id(self,user_id: int):
        """GET /users/{id}
        Get user by id
        :param user_id: int
        :return: UserModel dict
        """
        return self.api_request("GET", f"/users/{user_id}")

    def get_user_with_invalid_id(self, invalid_user_id):
        """GET /users/9999
        Get user with invalid id
        :param invalid_user_id: int For example: 9999
        :return: 404 status code
        """
        return self.api_request("GET", f"/users/{invalid_user_id}")
