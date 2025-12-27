def check(candidate):
    assert candidate(10) == 8
    assert candidate(19) == 16
    assert candidate(32) == 32


def highest_power_of_two(n):
    if n <= 0:
        return 0
    return 1 << (n - 1).bit_length()

check(highest_power_of_two)