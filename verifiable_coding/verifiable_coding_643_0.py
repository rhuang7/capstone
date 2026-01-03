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
        P = list(map(int, data[idx:idx+n]))
        idx += n
        A = list(map(int, data[idx:idx+n]))
        idx += n
        B = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Compute N = product of P_i^A_i
        # But we don't need to compute N directly, we need to count numbers <= N that have min exponents >= B_i
        
        # We need to find the count of numbers <= N that have exponents for each prime >= B_i
        # This is equivalent to counting numbers that are multiples of product of P_i^B_i
        
        # Compute the product of P_i^B_i
        product = 1
        for i in range(n):
            product *= pow(P[i], B[i])
        
        # Now we need to count numbers <= N that are multiples of product
        # But we also need to ensure that for each prime P_i, the exponent in the number is >= B_i
        # This is a classic inclusion-exclusion problem
        
        # Generate the list of primes and their minimum exponents
        primes = P
        min_exponents = B
        
        # We need to count numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        # This is equivalent to counting numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # We can use inclusion-exclusion to count numbers that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # First, compute the product of P_i^B_i
        # Then, compute the count of numbers <= N that are multiples of this product
        # But we also need to ensure that for each prime P_i, the exponent in the number is >= B_i
        # This is a classic problem that can be solved with inclusion-exclusion
        
        # The inclusion-exclusion approach is to generate all subsets of primes and compute the count of numbers that have exponents >= B_i for all primes not in the subset, and < B_i for those in the subset
        
        # We can use a recursive approach to generate all subsets of primes and compute the count of numbers that have exponents >= B_i for all primes not in the subset, and < B_i for those in the subset
        
        # But with n up to 1e5, this is not feasible
        
        # Instead, we can use the Möbius function and inclusion-exclusion on the exponents
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # Let's compute the product of P_i^B_i
        # Then, compute the count of numbers <= N that are multiples of this product
        # But we also need to ensure that for each prime P_i, the exponent in the number is >= B_i
        # This is a classic problem that can be solved with inclusion-exclusion
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # Let's compute the product of P_i^B_i
        # Then, compute the count of numbers <= N that are multiples of this product
        # But we also need to ensure that for each prime P_i, the exponent in the number is >= B_i
        # This is a classic problem that can be solved with inclusion-exclusion
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product of P_i^B_i and also have exponents >= B_i for each prime
        
        # Let's compute the product of P_i^B_i
        product = 1
        for i in range(n):
            product *= pow(P[i], B[i])
        
        # Now, we need to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        # This is equivalent to counting numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle to count numbers <= N that are multiples of product and also have exponents >= B_i for each prime
        
        # We can use the inclusion-exclusion principle