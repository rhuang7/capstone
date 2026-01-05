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
        
        # Generate all possible ways to split the dishes into two groups
        min_time = float('inf')
        for split in itertools.combinations(range(N), N//2):
            group1 = [C[i] for i in split]
            group2 = [C[i] for i in range(N) if i not in split]
            time1 = max(group1)
            time2 = max(group2)
            total_time = max(time1, time2)
            if total_time < min_time:
                min_time = total_time
        
        results.append(min_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()