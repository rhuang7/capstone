def check(candidate):
    assert candidate("person") =="PERSON"
    assert candidate("final") == "FINAL"
    assert candidate("Valid") == "VALID"


def to_uppercase(s):
    return s.upper()

check(to_uppercase)