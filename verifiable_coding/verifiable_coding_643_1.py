import sys
import math
from sys import stdin
from math import gcd
from bisect import bisect_right
MOD = 10**9 + 7

def main():
    import sys
    input = sys.stdin.read
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
        # But since N can be very large, we can't compute it directly
        # Instead, we need to find numbers <= N that have all primes in P with exponents >= B_i
        
        # We need to find the count of numbers <= N that have exponents >= B_i for all primes in P
        # This is equivalent to finding the count of numbers <= N that are divisible by product of P_i^B_i
        # But since the exponents can vary, we need to find the minimal exponents and count numbers that have exponents >= B_i for all primes
        
        # The minimal exponents for each prime is B_i
        # So we need to find numbers <= N that are divisible by product of P_i^B_i
        # But also, for each prime, the exponent in the number must be >= B_i
        # This is equivalent to counting numbers <= N that are divisible by product of P_i^B_i and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the product of P_i^B_i
        product = 1
        for i in range(n):
            product *= pow(P[i], B[i])
        
        # Now, we need to count numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        # This is equivalent to counting numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # We can use inclusion-exclusion to count the numbers that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # But since the exponents can be large, we need to use a sieve-like approach
        
        # We can use the inclusion-exclusion principle to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # But this is not feasible for large N, so we need a smarter approach
        
        # The minimal exponents for each prime is B_i, so the number must be divisible by product of P_i^B_i
        # So the numbers we are looking for are multiples of product, but also for each prime, the exponent in the number is >= B_i
        
        # So the problem reduces to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal exponent for each prime
        min_exponents = B
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal product that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, but also for each prime, the exponent in the number is >= B_i
        
        # So the numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal number that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, but also for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum possible value for each prime
        # For each prime, the maximum exponent is A_i
        # So the maximum number is product of P_i^A_i
        
        # Now, we need to find the count of numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the product of P_i^B_i
        product = 1
        for i in range(n):
            product *= pow(P[i], B[i])
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum number
        max_num = 1
        for i in range(n):
            max_num *= pow(P[i], A[i])
        
        # If max_num < product, then there are no such numbers
        if max_num < product:
            results.append(0)
            continue
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's use inclusion-exclusion to count the numbers that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # We can use the inclusion-exclusion principle to count the numbers that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # The minimal exponents for each prime is B_i
        # So the number must be divisible by product of P_i^B_i
        
        # The numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # So the numbers we are looking for are multiples of product, but also for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal number that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum number
        max_num = 1
        for i in range(n):
            max_num *= pow(P[i], A[i])
        
        # If max_num < product, then there are no such numbers
        if max_num < product:
            results.append(0)
            continue
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal number that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum number
        max_num = 1
        for i in range(n):
            max_num *= pow(P[i], A[i])
        
        # If max_num < product, then there are no such numbers
        if max_num < product:
            results.append(0)
            continue
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal number that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum number
        max_num = 1
        for i in range(n):
            max_num *= pow(P[i], A[i])
        
        # If max_num < product, then there are no such numbers
        if max_num < product:
            results.append(0)
            continue
        
        # Now, we need to count the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # This is equivalent to counting the numbers <= N that are divisible by product and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the minimal number that satisfies the exponents
        # This is product of P_i^B_i
        
        # Now, the numbers we are looking for are multiples of product, and for each prime, the exponent in the number is >= B_i
        
        # Let's compute the maximum number
        max_num = 1
        for i in range(n):
            max_num *= pow(P[i