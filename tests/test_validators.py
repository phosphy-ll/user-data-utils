import pytest
from user_data_utils.validators import validate_email, validate_password


@pytest.mark.parametrize("email", [
    "test@mail.com",
    "user.name@gmail.com",
])
def test_validate_email_valid(email):
    assert validate_email(email)


@pytest.mark.parametrize("email", [
    "bademail",
    "user@",
    "user.com",
])
def test_validate_email_invalid(email):
    assert not validate_email(email)


def test_validate_email_type_error():
    with pytest.raises(TypeError):
        validate_email(123)


def test_validate_password_valid():
    assert validate_password("StrongPass1")


def test_validate_password_invalid():
    assert not validate_password("weak")
