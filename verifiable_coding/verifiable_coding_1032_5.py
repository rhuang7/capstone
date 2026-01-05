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
        # We need to compute X * (N)^(N-1) mod 1e6+3
        # Compute pow(N, N-1, MOD)
        # But for large N, we can't compute it directly
        # Use fast exponentiation with modular reduction
        # However, for N up to 1e18, we need to compute pow(N, N-1, MOD)
        # But pow in Python can handle large exponents with modulus
        # So we compute pow(N, N-1, MOD)
        # Then multiply by X mod MOD
        power = pow(N, N-1, MOD)
        res = (X * power) % MOD
        results.append(res)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()