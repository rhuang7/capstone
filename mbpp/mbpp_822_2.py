def check(candidate):
    assert candidate("password")==False
    assert candidate("Password@10")==True
    assert candidate("password@10")==False


def is_password_valid(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
        return False
    return True

check(is_password_valid)