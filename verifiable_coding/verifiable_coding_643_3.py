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
        N = 1
        for p, a in zip(P, A):
            N = N * pow(p, a, MOD) % MOD
        
        # Compute the required sum
        # We need to count numbers <= N that have at least B_i power for each P_i
        # This is equivalent to counting numbers <= N that are multiples of product of P_i^B_i
        # But we need to count numbers that are multiples of product of P_i^B_i and also are divisors of N
        # So we need to find all multiples of product of P_i^B_i that divide N
        
        # Compute the product of P_i^B_i
        prod = 1
        for p, b in zip(P, B):
            prod = prod * pow(p, b, MOD) % MOD
        
        # Find all multiples of prod that divide N
        # This is equivalent to finding all divisors of N that are multiples of prod
        # So we need to find all divisors of N that are multiples of prod
        
        # Factorize N
        # But since N can be very large, we need to factorize it using the given primes P and their exponents A
        # Since N is product of P_i^A_i, we can directly use the prime factors of N
        # So we can generate all divisors of N using the given primes and their exponents
        
        # Generate all divisors of N
        divisors = [1]
        for i in range(n):
            p = P[i]
            a = A[i]
            temp = []
            for d in divisors:
                for j in range(1, a+1):
                    temp.append(d * pow(p, j, MOD))
            divisors += temp
        
        # Now filter the divisors to find those that are multiples of prod
        # Also, we need to count the numbers <= N that are multiples of prod and divide N
        # So for each divisor d of N that is a multiple of prod, we need to count how many numbers <= N are multiples of d
        
        # But since d divides N, the number of multiples of d <= N is N // d
        
        # So we need to find all divisors of N that are multiples of prod and count N // d for each such divisor
        
        count = 0
        for d in divisors:
            if d % prod == 0:
                count = (count + N // d) % MOD
        
        results.append(count)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    main()