def check(candidate):
    assert candidate(2, 3, 7) == ('x = ', 2, ', y = ', 1)
    assert candidate(4, 2, 7) == 'No candidate'
    assert candidate(1, 13, 17) == ('x = ', 4, ', y = ', 1)


def find_solution(a, b, n):
    from math import gcd

    g = gcd(a, b)
    if n % g != 0:
        return None

    # Extended Euclidean algorithm
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            g, x, y = extended_gcd(b, a % b)
            return (g, y, x - (a // b) * y)

    g, x, y = extended_gcd(a, b)
    x = x * (n // g)
    y = y * (n // g)
    return x, y

check(find_solution)