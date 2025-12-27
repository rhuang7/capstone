def check(candidate):
    assert candidate("python")==False
    assert candidate("1")==True
    assert candidate("12345")==True


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

check(is_integer)