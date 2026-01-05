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
        # Each burner has a list of dishes, and the time is the sum of the times of the dishes on that burner
        # The total time is the maximum of the two sums
        # We need to find the split that minimizes this maximum
        # Try all possible ways to split the dishes into two groups
        # Since N is small (<=4), we can try all possible combinations
        min_time = float('inf')
        for i in range(1, 1 << N):
            # i is the bitmask of dishes on the first burner
            sum1 = 0
            sum2 = 0
            for j in range(N):
                if i & (1 << j):
                    sum1 += C[j]
                else:
                    sum2 += C[j]
            min_time = min(min_time, max(sum1, sum2))
        results.append(min_time)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()