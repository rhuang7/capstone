def check(candidate):
    assert candidate(2) == 7
    assert candidate(4) == 223
    assert candidate(5) == 959


def carol_number(n):
    return (2 ** (2 ** n)) % 256 - 2 ** (2 ** n) + 1

check(carol_number)