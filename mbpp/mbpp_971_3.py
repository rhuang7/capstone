def check(candidate):
    assert candidate(7, 5, 2, 5) == 2
    assert candidate(17, 2, 1, 3) == 17
    assert candidate(18, 16, 3, 6) == 6


def max_segments(n, a, b, c):
    count = 0
    while n >= a + b + c:
        n -= a + b + c
        count += 1
    return count

check(max_segments)