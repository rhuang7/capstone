import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])

    mod = M

    # Total number of strings of length N is 2^N
    total = pow(2, N, mod)

    # Subtract the number of periodic strings
    # A string is periodic if it can be written as v^n for some n >= 2
    # So we need to find all strings that are not of the form v^n for any n >= 2

    # We use inclusion-exclusion principle
    # For each divisor d of N (d >= 2), we subtract the number of strings of length d that can be repeated to form a string of length N

    from math import gcd
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def get_divisors(n):
        divisors = set()
        for i in range(2, n + 1):
            if n % i == 0:
                divisors.add(i)
        return sorted(divisors)

    divisors = get_divisors(N)

    # For each divisor d of N, compute the number of strings of length d that can be repeated to form a string of length N
    # This is equal to the number of strings of length d that are not periodic (i.e., not of the form v^k for k >= 2)
    # But since d is a divisor of N, we can compute it recursively

    # We use memoization to avoid recomputation
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def count_non_periodic(n):
        if n == 1:
            return 2
        total = pow(2, n, mod)
        divisors = get_divisors(n)
        for d in divisors:
            if d >= 2:
                total = (total - count_non_periodic(d) * pow(2, n // d - 1, mod)) % mod
        return total

    result = (total - count_non_periodic(N)) % mod
    print(result)

if __name__ == '__main__':
    solve()