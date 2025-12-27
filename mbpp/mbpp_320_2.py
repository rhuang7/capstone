def check(candidate):
    assert candidate(12)==5434
    assert candidate(20)==41230
    assert candidate(54)==2151270


def calculate_difference(n):
    squared_sum = n * (n + 1) // 2 ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return squared_sum - sum_of_squares

check(calculate_difference)