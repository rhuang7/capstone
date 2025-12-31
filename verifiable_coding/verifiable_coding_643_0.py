import sys
import math
from bisect import bisect_right

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
        # But since N can be huge, we need to compute it modulo MOD-1 (for exponents)
        # But since we need to count numbers <= N, we need to find N first
        # However, since N can be extremely large, we can't compute it directly
        # So we use the inclusion-exclusion principle with the constraints of B
        
        # We need to find the sum of all numbers x <= N such that for each prime p_i, the minimum exponent of p_i in x is >= B_i
        
        # We can model this as a multiplicative function problem
        # The answer is the sum of all numbers x <= N such that for all i, the exponent of p_i in x is >= B_i
        
        # We can use the inclusion-exclusion principle with the constraints of B
        
        # First, compute the product of P_i^B_i to get the lower bound
        # Then compute the product of P_i^(A_i - B_i) to get the upper bound
        # The numbers we are counting are those that are multiples of the lower bound and <= N
        
        # But since N is the product of P_i^A_i, we can compute it as:
        # N = product(P_i^A_i)
        
        # But since N can be very large, we can't compute it directly
        # So we need to find the sum of numbers x <= N that are multiples of the lower bound
        
        # Let's compute the lower bound L = product(P_i^B_i)
        # Let's compute the upper bound U = product(P_i^(A_i - B_i))
        # The numbers we are counting are those that are multiples of L and <= N
        
        # But since N is product(P_i^A_i), we can compute it as:
        # N = L * U
        
        # So the problem reduces to finding the sum of all multiples of L that are <= L * U
        
        # The sum of multiples of L up to L * U is L * (U * (U + 1)) // 2
        
        # However, this is only valid if all exponents are >= B_i, which is the case here
        
        # So the answer is L * (U * (U + 1)) // 2
        
        # But we need to compute L and U
        
        # Compute L = product(P_i^B_i)
        L = 1
        for i in range(n):
            L *= pow(P[i], B[i], MOD)
        
        # Compute U = product(P_i^(A_i - B_i))
        U = 1
        for i in range(n):
            U *= pow(P[i], A[i] - B[i], MOD)
        
        # Compute the sum of multiples of L up to L * U
        # But since L * U can be very large, we can't compute it directly
        # So we need to compute it modulo MOD
        
        # The sum is L * (U * (U + 1)) // 2 mod MOD
        # But since MOD is a prime, we can compute the modular inverse of 2
        
        inv2 = pow(2, MOD-2, MOD)
        sum_val = (L * U) % MOD
        sum_val = sum_val * (sum_val + 1) % MOD
        sum_val = sum_val * inv2 % MOD
        sum_val = sum_val * L % MOD
        
        results.append(sum_val)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    main()