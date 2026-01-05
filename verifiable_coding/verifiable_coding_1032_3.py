import sys

MOD = 10**6 + 3

def solve():
    import sys
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
        # But since N can be up to 1e18, we need a fast way to compute (N)^(N-1) mod MOD
        # We can use modular exponentiation
        power = pow(N, N-1, MOD)
        results.append((X * power) % MOD)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()