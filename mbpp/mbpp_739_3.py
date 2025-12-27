def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 14
    assert candidate(4) == 45


def smallest_triangular_index(n):
    def triangular_number(k):
        return k * (k + 1) // 2

    def num_digits(x):
        return len(str(x))

    k = 1
    while num_digits(triangular_number(k)) < n:
        k += 1
    return k - 1

check(smallest_triangular_index)