def check(candidate):
    assert candidate(7) == 2.5928571428571425
    assert candidate(4) == 2.083333333333333
    assert candidate(19) == 3.547739657143682


def harmonic_sum(n):
    if n <= 0:
        return 0.0
    return sum(1.0 / i for i in range(1, n))

check(harmonic_sum)