import pytest
from models.users import UserModel
from apis.users import UsersApi


@pytest.mark.smoke
@pytest.mark.full
def test_get_all_users():
    # Send API request to retrieve all users
    users = UsersApi().get_all_users().json()

    assert users, "No users returned"

    # Validate returned users data against the model
    for user in users:
        UserModel.model_validate(user)
