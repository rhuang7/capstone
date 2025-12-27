def check(candidate):
    assert candidate(10,15) == 6
    assert candidate(100,150) == 93
    assert candidate(4,6) == 3


def sum_common_divisors(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def get_divisors(n):
        divisors = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)
        return divisors

    common_divisors = get_divisors(a) & get_divisors(b)
    return sum(common_divisors)

check(sum_common_divisors)