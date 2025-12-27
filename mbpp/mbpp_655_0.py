def check(candidate):
    assert candidate(2) == 33
    assert candidate(4) == 1300
    assert candidate(3) == 276


def sum_of_fifth_powers(n):
    return sum(i**5 for i in range(1, n + 1))

check(sum_of_fifth_powers)