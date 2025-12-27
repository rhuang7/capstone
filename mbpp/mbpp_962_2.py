def check(candidate):
    assert candidate(2,5) == 6
    assert candidate(3,8) == 18
    assert candidate(4,6) == 10


def sum_even_numbers(l, r):
    return sum(num for num in range(l, r + 1) if num % 2 == 0)

check(sum_even_numbers)