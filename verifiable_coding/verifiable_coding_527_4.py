import sys
import math
from collections import defaultdict

def factorize(n):
    factors = defaultdict(int)
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        factors[n] += 1
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    
    N = int(data[idx])
    idx += 1
    
    A = []
    for _ in range(N):
        A.append(int(data[idx]))
        idx += 1
    
    Q = int(data[idx])
    idx += 1
    
    # Precompute prime factors for all numbers up to 1000000
    max_prime = 1000000
    primes = []
    is_prime = [True] * (max_prime + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, max_prime + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, max_prime + 1, i):
                is_prime[j] = False
    
    # Factorize each number in the array
    prime_counts = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        n = A[i]
        factors = factorize(n)
        for p, cnt in factors.items():
            prime_counts[i][p] = cnt
    
    # Build prefix sums for each prime
    prefix = [defaultdict(int) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for p in prime_counts[i - 1]:
            prefix[i][p] = prefix[i - 1][p] + prime_counts[i - 1][p]
    
    for _ in range(Q):
        k = int(data[idx])
        idx += 1
        if k == 1:
            l = int(data[idx]) - 1
            r = int(data[idx + 1]) - 1
            idx += 2
            # Compute the product's prime factors
            factors = defaultdict(int)
            for i in range(l, r + 1):
                for p, cnt in prime_counts[i].items():
                    factors[p] += cnt
            # Check if all exponents are even
            is_square = True
            for p in factors:
                if factors[p] % 2 != 0:
                    is_square = False
                    break
            print("YES" if is_square else "NO")
        else:
            i = int(data[idx]) - 1
            val = int(data[idx + 1])
            idx += 2
            # Update the value at position i
            A[i] *= val
            # Factorize the new value
            new_factors = factorize(A[i])
            # Update prime_counts[i]
            prime_counts[i] = new_factors
            # Update prefix sums
            for p in new_factors:
                prefix[i + 1][p] = prefix[i][p] + new_factors[p]
            for j in range(i + 1, N + 1):
                for p in new_factors:
                    prefix[j][p] = prefix[j - 1][p] + new_factors[p]