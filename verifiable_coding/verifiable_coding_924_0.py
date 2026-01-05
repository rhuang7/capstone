import sys
import math
from sys import stdin

def get_prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    i = 3
    max_factor = math.isqrt(n) + 1
    while i <= max_factor and n > 1:
        while n % i == 0:
            factors.add(i)
            n //= i
            max_factor = math.isqrt(n) + 1
        i += 2
    if n > 1:
        factors.add(n)
    return factors

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    K = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1

    K_factors = get_prime_factors(K)
    prime_factors = list(K_factors)
    prime_set = set(prime_factors)

    # Initialize the array as empty
    # We'll use a segment tree to track which primes are present in ranges
    # Since K can have up to 10^5 prime factors (unlikely), we need to track for each prime if it's present in a range
    # But since K is up to 1e9, we can precompute its prime factors

    # For each query, we need to know for each prime in K_factors if it's present in the range [l, r]
    # We can use a segment tree that tracks for each range the set of primes present
    # However, with 1e5 queries and 1e5 primes, this is not feasible

    # Alternative approach: For each query of type ?, we need to check for each prime in K_factors if it's present in any position in [l, r]
    # So we can maintain for each prime in K_factors a segment tree that tracks if it's present in a range

    # But with 1e5 primes, this is not feasible

    # So instead, we can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need a more efficient way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a list of intervals where it is set
    # Then for a query [l, r], we check if any of the intervals for a prime overlaps with [l, r]

    # However, with 1e5 queries and 1e5 primes, this is not feasible either

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then, for each query of type ?, we need to check for each prime in K_factors if it is present in any position in [l, r]

    # We can maintain for each prime in K_factors a segment tree that tracks if it's present in a range
    # But since K can have up to 10^5 primes (unlikely), this is not feasible

    # So we need to find another way

    # Let's precompute the prime factors of K
    # Then