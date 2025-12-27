def check(candidate):
    assert candidate("InValid") == "invalid"
    assert candidate("TruE") == "true"
    assert candidate("SenTenCE") == "sentence"


def to_lowercase(s):
    return s.lower()

check(to_lowercase)