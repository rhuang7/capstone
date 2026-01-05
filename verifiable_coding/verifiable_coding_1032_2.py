import sys
import math

MOD = 10**6 + 3

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        X = int(data[idx+1])
        idx += 2
        if N == 0:
            results.append(X % MOD)
            continue
        # The number of particles at time t is X * (t)^(t-1)
        # But since N can be up to 1e18, we need to compute this efficiently
        # Using modular exponentiation
        # However, since (t)^(t-1) is huge, we need to compute it modulo MOD
        # But for t up to 1e18, we can't compute it directly
        # So we need to find a pattern or use some mathematical insight
        # Let's see:
        # For N=1, result is X * 1^0 = X
        # For N=2, result is X * 2^1 = 2X
        # For N=3, result is X * 3^2 = 9X
        # For N=4, result is X * 4^3 = 64X
        # So the pattern is X * (N)^(N-1)
        # But since N can be up to 1e18, we need to compute (N)^(N-1) mod MOD
        # However, for large exponents, we can't compute it directly
        # So we need to use Fermat's little theorem
        # Since MOD is a prime (10^6+3 = 1000003 is a prime)
        # So a^(MOD-1) ≡ 1 mod MOD
        # So we can compute the exponent mod (MOD-1)
        # But only if a and MOD are coprime
        # Since MOD is prime, if a is not a multiple of MOD, then a and MOD are coprime
        # So for a = N, if N is not divisible by MOD, then we can compute N^(N-1) mod MOD as pow(N, N-1, MOD)
        # If N is divisible by MOD, then N^(N-1) mod MOD is 0
        # So the formula is:
        # result = (X * pow(N, N-1, MOD)) % MOD
        # But for N up to 1e18, we need to compute pow(N, N-1, MOD)
        # However, in Python, pow can handle large exponents with three arguments
        # So we can use that
        if N % MOD == 0:
            results.append(0)
        else:
            results.append((X * pow(N, N-1, MOD)) % MOD)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()