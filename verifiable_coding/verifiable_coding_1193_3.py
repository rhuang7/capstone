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
        # Initialize capacity array
        capacity = [1] * N
        for l, r in ranges:
            # Find the minimum in the range [l, r]
            min_val = min(capacity[l:r+1])
            # Update the range [l, r] with min_val % MOD
            for i in range(l, r + 1):
                capacity[i] = (capacity[i] + min_val) % MOD
        # Find the minimum capacity after Y days
        min_cap = min(capacity)
        results.append(min_cap % MOD)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()