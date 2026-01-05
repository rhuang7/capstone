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
        # However, since the exponent is (N-1), and the base is N, we need to compute N^(N-1) mod MOD
        # But N can be up to 1e18, so we need to compute pow(N, N-1, MOD)
        # However, pow in Python can handle large exponents efficiently
        # So the answer is (X * pow(N, N-1, MOD)) % MOD
        result = (X * pow(N, N-1, MOD)) % MOD
        results.append(result)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()