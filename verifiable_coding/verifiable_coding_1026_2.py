import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N1 = int(input[idx])
        N2 = int(input[idx+1])
        N3 = int(input[idx+2])
        idx += 3
        # Total triples: N1 * N2 * N3
        # Subtract triples with at least two equal numbers
        # Using inclusion-exclusion principle
        total = (N1 * N2 % MOD) * N3 % MOD
        same12 = (N1 * N2) % MOD
        same13 = (N1 * N3) % MOD
        same23 = (N2 * N3) % MOD
        same_all = (N1 * N2 * N3) % MOD
        # Subtract cases where at least two are same
        total = (total - same12 - same13 - same23 + same_all) % MOD
        print(total)

if __name__ == '__main__':
    solve()