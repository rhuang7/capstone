def check(candidate):
    assert candidate(11) == 10
    assert candidate(7) == 6
    assert candidate(12) == 11


def find_closest_smaller(n):
    if n <= 0:
        return None  # No smaller number exists for non-positive n
    return n - 1

check(find_closest_smaller)