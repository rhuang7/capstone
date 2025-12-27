def check(candidate):
    assert candidate(3, 1) == 4
    assert candidate(4, 1) == 11
    assert candidate(5, 3) == 26


def eulerian_number(n, m):
    if m < 0 or m > n - 1:
        return 0
    if m == 0:
        return 1
    return (n - m) * eulerian_number(n - 1, m - 1) - (m + 1) * eulerian_number(n - 1, m)

check(eulerian_number)