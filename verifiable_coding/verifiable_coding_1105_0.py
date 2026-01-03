import sys

def solve():
    import itertools
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        C = list(map(int, input[idx:idx+N]))
        idx += N
        if N == 0:
            results.append(0)
            continue
        if N == 1:
            results.append(C[0])
            continue
        if N == 2:
            results.append(max(C))
            continue
        # For N = 3 or 4, try all possible ways to split into two burners
        # We need to find the minimum time such that the sum of times on each burner is minimized
        # We can try all possible partitions of the dishes into two groups
        min_time = float('inf')
        # Generate all possible ways to split the dishes into two groups
        for mask in range(1, 1 << N):
            group1 = []
            group2 = []
            for i in range(N):
                if (mask >> i) & 1:
                    group1.append(C[i])
                else:
                    group2.append(C[i])
            time1 = sum(group1)
            time2 = sum(group2)
            min_time = min(min_time, max(time1, time2))
        results.append(min_time)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()