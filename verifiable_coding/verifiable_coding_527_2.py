import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0

    N = int(data[idx])
    idx += 1

    A = list(map(int, data[idx:idx+N]))
    idx += N

    Q = int(data[idx])
    idx += 1

    queries = []
    for _ in range(Q):
        k = int(data[idx])
        if k == 1:
            l = int(data[idx+1])
            r = int(data[idx+2])
            queries.append((k, l, r))
            idx += 3
        else:
            i = int(data[idx+1])
            val = int(data[idx+2])
            queries.append((k, i, val))
            idx += 3

    # Preprocess prime factors for numbers up to 1e6
    max_num = 1000000
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num+1, i):
                is_prime[j] = False

    # Sieve of Eratosthenes to find primes up to 100
    primes = []
    for i in range(2, 101):
        if is_prime[i]:
            primes.append(i)

    # Function to get prime factors of a number
    def get_factors(x):
        factors = defaultdict(int)
        for p in primes:
            if p * p > x:
                break
            while x % p == 0:
                factors[p] += 1
                x //= p
        if x > 1:
            factors[x] += 1
        return factors

    # Precompute prime factors for each element in the array
    factors = [get_factors(x) for x in A]

    # For each query of type 1, we need to compute the product of factors in range [l, r]
    # and check if all exponents are even
    # We will use a prefix sum approach for each prime
    # Since primes are up to 100, we can have a prefix sum array for each prime
    prime_count = defaultdict(list)
    for i in range(N):
        for p in factors[i]:
            prime_count[p].append(factors[i][p])

    # Build prefix sums for each prime
    for p in prime_count:
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + prime_count[p][i]
        prime_count[p] = prefix

    # Process queries
    output = []
    for query in queries:
        if query[0] == 1:
            l = query[1] - 1
            r = query[2] - 1
            is_square = True
            for p in prime_count:
                cnt = prime_count[p][r+1] - prime_count[p][l]
                if cnt % 2 != 0:
                    is_square = False
                    break
            output.append("YES" if is_square else "NO")
        else:
            i = query[1] - 1
            val = query[2]
            # Update the value at index i
            A[i] *= val
            # Update the factors
            old_factors = factors[i]
            new_factors = get_factors(A[i])
            # Update the prime counts
            for p in prime_count:
                if p in old_factors:
                    prime_count[p][i+1] -= old_factors[p]
                if p in new_factors:
                    prime_count[p][i+1] += new_factors[p]
            factors[i] = new_factors

    print("\n".join(output))