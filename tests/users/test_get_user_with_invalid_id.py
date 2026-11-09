import pytest
import pytest_check as check
from apis.users import UsersApi


@pytest.mark.full
@pytest.mark.negative
@pytest.mark.parametrize("invalid_id", [9999, -1, "abc"])
def test_get_user_with_invalid_id(invalid_id):
    # Send API request retrieve user with invalid id
    invalid_id = 9999
    response = UsersApi().get_user_with_invalid_id(invalid_id)

    # Validate that not found status is returned
    assert response.status_code == 404, \
        f"Expected 404 for user id {invalid_id}, got {response.status_code}"

    # Validate that returned body should be empty
    check.equal(response.json(), {}, f"Expected empty body, got {response.json()}")
