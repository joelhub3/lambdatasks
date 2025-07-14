import string
import secrets

_alphabet = string.ascii_letters + string.digits + "@$%^*=?.;"


def random_temporary_password(num_chars=12):
    return "".join(secrets.choice(_alphabet) for i in range(num_chars))
