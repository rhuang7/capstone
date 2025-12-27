def check(candidate):
    assert candidate(5,2) == 10
    assert candidate(4,3) == 4
    assert candidate(3,2) == 3


def binomial_coefficient(n, k):
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result

check(binomial_coefficient)