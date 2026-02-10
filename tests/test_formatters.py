import pytest
from user_data_utils.formatters import normalize_name


def test_normalize_name():
    assert normalize_name("  john doe ") == "John Doe"


def test_normalize_name_type_error():
    with pytest.raises(TypeError):
        normalize_name(123)
