import re


def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    return re.match(pattern, email) is not None


def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_upper and has_lower and has_digit
