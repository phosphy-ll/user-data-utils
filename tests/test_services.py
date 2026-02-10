from unittest.mock import Mock
import pytest
from user_data_utils.services import register_user


def test_register_user_success():
    mock_sender = Mock()
    result = register_user("test@mail.com", "Pass1234", mock_sender)

    mock_sender.send.assert_called_once_with("test@mail.com")
    assert result is True


def test_register_user_invalid_email():
    mock_sender = Mock()

    with pytest.raises(ValueError):
        register_user("bademail", "Pass1234", mock_sender)
