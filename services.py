from .validators import validate_email


def register_user(email: str, password: str, email_sender) -> bool:
    """
    email_sender — внешний сервис (зависимость),
    который отправляет письмо.
    """

    if not validate_email(email):
        raise ValueError("Invalid email")

    email_sender.send(email)

    return True
