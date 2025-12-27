def check(candidate):
    assert candidate(5,100) == 8
    assert candidate(8,65) == 6
    assert candidate(2,5) == 1


def count_odd_factor_numbers(n):
    return (n // 2) if n % 2 == 0 else (n // 2) + 1

check(count_odd_factor_numbers)