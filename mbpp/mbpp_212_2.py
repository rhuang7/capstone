def check(candidate):
    assert candidate(2) == 17
    assert candidate(4) == 354
    assert candidate(6) == 2275


def sum_of_fourth_powers(n):
    return sum(i**4 for i in range(1, n + 1))

check(sum_of_fourth_powers)