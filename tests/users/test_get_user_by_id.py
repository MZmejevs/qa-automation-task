import pytest
import pytest_check as check
from models.users import UserModel
from apis.users import UsersApi


@pytest.mark.full
@pytest.mark.parametrize("user_id", [pytest.param(1, marks=pytest.mark.smoke), 5, 10])
def test_get_user_by_id(user_id):
    # Send API request to retrieve user by id
    user_id = 1
    user = UsersApi().get_user_by_id(user_id).json()

    assert user, f"No users returned with id: {user_id}"

    # Validate returned user data against the model
    UserModel.model_validate(user)

    # Validate that the returned user is the one we asked for
    check.equal(user["id"], user_id, f"Expected user id {user_id}, got {user['id']}")
