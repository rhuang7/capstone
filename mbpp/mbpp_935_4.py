def check(candidate):
    assert candidate(6)==91
    assert candidate(7)==140
    assert candidate(12)==650


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 2

check(sum_of_squares)