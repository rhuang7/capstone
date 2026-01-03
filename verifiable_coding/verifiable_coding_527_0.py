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
    
    # Precompute prime factors for each number in A
    prime_factors = []
    for num in A:
        factors = defaultdict(int)
        n = num
        for p in primes:
            if p * p > n:
                break
            while n % p == 0:
                factors[p] += 1
                n //= p
        if n > 1:
            factors[n] += 1
        prime_factors.append(factors)
    
    # Build prefix sums for each prime
    primes_set = set(primes)
    prefix = defaultdict(list)
    for p in primes_set:
        prefix[p] = [0] * (N + 1)
    
    for i in range(1, N + 1):
        for p in primes_set:
            prefix[p][i] = prefix[p][i - 1]
        for p in prime_factors[i - 1]:
            prefix[p][i] += prime_factors[i - 1][p]
    
    def get_product_factors(l, r):
        res = defaultdict(int)
        for p in primes_set:
            res[p] = prefix[p][r] - prefix[p][l - 1]
        return res
    
    def is_perfect_square(factors):
        for p in factors:
            if factors[p] % 2 != 0:
                return False
        return True
    
    output = []
    for _ in range(Q):
        k = int(data[idx])
        idx += 1
        if k == 1:
            l = int(data[idx])
            idx += 1
            r = int(data[idx])
            idx += 1
            factors = get_product_factors(l, r)
            if is_perfect_square(factors):
                output.append("YES")
            else:
                output.append("NO")
        else:
            i = int(data[idx])
            idx += 1
            val = int(data[idx])
            idx += 1
            # Update the value at position i-1
            A[i - 1] *= val
            # Factorize the new value
            new_factors = factorize(A[i - 1])
            # Update the prefix sums
            for p in primes_set:
                prefix[p][i] += new_factors.get(p, 0)
                for j in range(i + 1, N + 1):
                    prefix[p][j] += new_factors.get(p, 0)
    
    print('\n'.join(output))