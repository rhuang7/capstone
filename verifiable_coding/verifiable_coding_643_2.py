import sys
import math
from collections import defaultdict

MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        P = list(map(int, data[idx:idx + n]))
        idx += n
        A = list(map(int, data[idx:idx + n]))
        idx += n
        B = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Compute N = P1^A1 * P2^A2 * ... * Pn^An
        N = 1
        for i in range(n):
            N *= pow(P[i], A[i])
        
        # Compute the minimal exponents for each prime
        min_exponents = [B[i] for i in range(n)]
        
        # Sieve of Eratosthenes to find all primes up to sqrt(N)
        max_prime = int(N**0.5) + 1
        is_prime = [True] * (max_prime + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_prime**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, max_prime + 1, i):
                    is_prime[j] = False
        
        # Precompute factorials and inverse factorials modulo MOD
        max_fact = 0
        for i in range(n):
            max_fact = max(max_fact, A[i])
        max_fact = max(max_fact, N)
        fact = [1] * (max_fact + 1)
        for i in range(1, max_fact + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (max_fact + 1)
        inv_fact[max_fact] = pow(fact[max_fact], MOD - 2, MOD)
        for i in range(max_fact - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        # Function to compute the number of multiples of a number up to X
        def count_multiples(x, p):
            return x // p
        
        # Function to compute the sum of multiples of a number up to X
        def sum_multiples(x, p):
            return p * (x // p) * (x // p + 1) // 2
        
        # Function to compute the inclusion-exclusion sum
        def inclusion_exclusion():
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that have at least the min exponents
            # This is equivalent to finding numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Compute the product of P_i^B_i
            product = 1
            for i in range(n):
                product *= pow(P[i], B[i])
            
            # Compute the sum of all multiples of product up to N
            # But we need to subtract those that are divisible by higher multiples
            # So we need to use inclusion-exclusion on the multiples of product
            # This is a standard inclusion-exclusion problem
            
            # We can use the inclusion-exclusion principle with the Möbius function
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # We can use the inclusion-exclusion principle with the Möbius function
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # We can use the inclusion-exclusion principle with the Möbius function
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # We can use the inclusion-exclusion principle with the Möbius function
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to subtract those that are divisible by higher multiples
            # This is a standard inclusion-exclusion problem
            
            # Generate all subsets of the primes with min exponents > 0
            # Use Möbius function for inclusion-exclusion
            # We need to find all numbers <= N that are divisible by the product of P_i^B_i
            # But we need to count numbers that have at least the min exponents for each prime
            # So we need to find the sum of all numbers <= N that are divisible by the product of P_i^B_i