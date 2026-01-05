import sys
MOD = 10**9 + 7

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        Y = int(data[idx])
        idx += 1
        ranges = []
        for _ in range(Y):
            l = int(data[idx])
            r = int(data[idx + 1])
            ranges.append((l, r))
            idx += 2
        # Initialize capacities
        capacities = [1] * N
        for l, r in ranges:
            min_val = min(capacities[l:r+1])
            min_val %= MOD
            for i in range(l, r + 1):
                capacities[i] = (capacities[i] + min_val) % MOD
        min_cap = min(capacities)
        results.append(str(min_cap % MOD))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()