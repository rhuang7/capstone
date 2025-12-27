def check(candidate):
    assert candidate(5) == 65
    assert candidate(10) == 280
    assert candidate(15) == 645


def nth_octagonal_number(n):
    return n * (3 * n - 2)

check(nth_octagonal_number)