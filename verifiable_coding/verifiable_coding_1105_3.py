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
        # For N >= 3, try all possible ways to split dishes into two groups
        # and find the minimum time
        min_time = float('inf')
        # Generate all possible partitions of dishes into two groups
        for i in range(1, 1 << N):
            group1 = []
            group2 = []
            for j in range(N):
                if (i >> j) & 1:
                    group1.append(C[j])
                else:
                    group2.append(C[j])
            # Compute the time for each group
            time1 = sum(group1)
            time2 = sum(group2)
            # The total time is the maximum of the two times
            total_time = max(time1, time2)
            if total_time < min_time:
                min_time = total_time
        results.append(min_time)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()