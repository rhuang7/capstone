def check(candidate):
    assert candidate(383) == True
    assert candidate(254) == False
    assert candidate(200) == False


def is_woodball(n):
    if n < 0:
        return False
    return n % 2 == 0

check(is_woodball)