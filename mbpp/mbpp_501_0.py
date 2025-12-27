def check(candidate):
    assert candidate(2,4) == 2
    assert candidate(2,8) == 2
    assert candidate(12,24) == 6


def find_common_divisor(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return gcd(a, b)

check(find_common_divisor)