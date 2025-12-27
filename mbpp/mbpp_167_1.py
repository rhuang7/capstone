def check(candidate):
    assert candidate(0) == 1
    assert candidate(5) == 8
    assert candidate(17) == 32


def smallest_power_of_two(n):
    if n <= 0:
        return 1
    power = 1
    while power < n:
        power <<= 1
    return power

check(smallest_power_of_two)