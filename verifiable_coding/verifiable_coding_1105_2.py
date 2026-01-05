import sys

def solve():
    import itertools
    input = sys.stdin.buffer.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        C = list(map(int, input[idx:idx+N]))
        idx += N
        if N == 0:
            print(0)
            continue
        if N == 1:
            print(C[0])
            continue
        if N == 2:
            print(max(C))
            continue
        # For N = 3 or 4, try all possible ways to split into two burners
        min_time = float('inf')
        # Generate all possible ways to split the dishes into two groups
        for split in itertools.combinations(range(N), 1):
            group1 = [C[i] for i in split]
            group2 = [C[i] for i in range(N) if i not in split]
            # Calculate the time for each group
            time1 = sum(group1)
            time2 = sum(group2)
            # The total time is the maximum of the two times
            total_time = max(time1, time2)
            min_time = min(min_time, total_time)
        print(min_time)

if __name__ == '__main__':
    solve()