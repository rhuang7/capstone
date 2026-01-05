import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    M = int(data[1])

    mod = M

    # Precompute the number of non-periodic strings of length N
    # A string is non-periodic if it cannot be written as v^n for some n >= 2
    # So, total strings - periodic strings = non-periodic strings

    # Total strings of length N is 2^N
    total = pow(2, N, mod)

    # Compute the number of periodic strings
    # A string is periodic if it can be written as v^n for some n >= 2
    # So, for each d dividing N, d > 1, we subtract the number of strings of length d that can be repeated to form a string of length N

    # Use inclusion-exclusion to avoid overcounting
    from math import gcd
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def count_periodic(d):
        # Count the number of strings of length d that can be repeated to form a string of length N
        # This is equal to the number of strings of length d that are not primitive
        # A string is primitive if it cannot be written as v^k for some k >= 2
        # So, the number of non-primitive strings of length d is 2^d - phi(d) * 2^{d / gcd(d, k)} ... ?

        # We use Möbius inversion to find the number of primitive strings of length d
        # The number of primitive strings of length d is sum_{k | d} mu(k) * 2^{d/k}
        # So, the number of non-primitive strings is 2^d - sum_{k | d} mu(k) * 2^{d/k}

        # So, the number of periodic strings is sum_{d | N, d > 1} (number of strings of length d that can be repeated to form a string of length N)
        # Which is sum_{d | N, d > 1} (number of non-primitive strings of length d)
        # Which is sum_{d | N, d > 1} (2^d - sum_{k | d} mu(k) * 2^{d/k})

        # So, for each divisor d of N, d > 1, we compute the number of periodic strings of length N that are formed by repeating a string of length d
        # But we need to avoid overcounting, so we use inclusion-exclusion

        # For each divisor d of N, d > 1, we compute the number of strings of length N that are periodic with period d
        # This is equal to the number of primitive strings of length d, raised to the power of N/d

        # But this is not correct, so we use the Möbius function to find the number of primitive strings of length d
        # Then, the number of periodic strings of length N with period d is equal to the number of primitive strings of length d

        # So, the total number of periodic strings is sum_{d | N, d > 1} (number of primitive strings of length d)

        # So, we need to compute for each divisor d of N, d > 1, the number of primitive strings of length d
        # Which is sum_{k | d} mu(k) * 2^{d/k}

        # So, the total number of periodic strings is sum_{d | N, d > 1} (sum_{k | d} mu(k) * 2^{d/k})

        # So, we need to compute for each divisor d of N, d > 1, the sum over k dividing d of mu(k) * 2^{d/k}

        # So, first, find all divisors of N
        divisors = set()
        for i in range(1, int(N**0.5) + 1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
        divisors.discard(1)
        divisors = sorted(divisors)

        res = 0
        for d in divisors:
            # Compute sum_{k | d} mu(k) * 2^{d/k}
            # First, find all divisors of d
            divs = set()
            for i in range(1, int(d**0.5) + 1):
                if d % i == 0:
                    divs.add(i)
                    divs.add(d // i)
            divs = sorted(divs)
            total = 0
            for k in divs:
                # Compute mu(k)
                # mu(k) is 0 if k has a squared prime factor
                # mu(k) is (-1)^r if k is square-free with r prime factors
                # So, factor k
                temp = k
                is_square_free = True
                factors = set()
                for p in range(2, int(temp**0.5) + 1):
                    if temp % p == 0:
                        count = 0
                        while temp % p == 0:
                            temp //= p
                            count += 1
                        if count > 1:
                            is_square_free = False
                        factors.add(p)
                if not is_square_free:
                    mu = 0
                else:
                    mu = (-1)**len(factors)
                # Compute 2^(d/k)
                power = d // k
                term = mu * pow(2, power, mod)
                total = (total + term) % mod
            res = (res + total) % mod
        return res

    periodic = count_periodic(N)
    non_periodic = (total - periodic) % mod
    print(non_periodic)

if __name__ == '__main__':
    solve()