def check(candidate):
    assert candidate(15, 10, 5) == 15
    assert candidate(187, 10, 5) == 185
    assert candidate(16, 11, 1) == 12


def find_largest_k(x, y):
    if y > x:
        return -1  # No solution since y cannot be greater than x
    return (x * 10) + y  # Largest k is 10*x + y, as it satisfies k % x == y

check(find_largest_k)