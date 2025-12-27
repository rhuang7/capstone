def check(candidate):
    assert candidate(2,5) == 8
    assert candidate(5,7) == 12
    assert candidate(7,13) == 40


def sum_odd_numbers(l, r):
    return sum(num for num in range(l, r + 1) if num % 2 != 0)

check(sum_odd_numbers)