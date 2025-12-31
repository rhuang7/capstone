import sys

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
        C = list(map(int, data[idx:idx+N]))
        idx += N
        
        if N == 0:
            results.append(0)
            continue
        
        # For small N (up to 4), we can try all permutations
        from itertools import permutations
        
        min_time = float('inf')
        
        # Try all possible ways to assign dishes to two burners
        # Each assignment is a tuple of two lists (burner1, burner2)
        # We generate all possible partitions of the dishes into two groups
        from itertools import combinations
        
        for k in range(0, N+1):
            for subset in combinations(range(N), k):
                burner1 = list(C[i] for i in subset)
                burner2 = list(C[i] for i in range(N) if i not in subset)
                
                # Calculate the time for each burner
                time1 = sum(burner1)
                time2 = sum(burner2)
                
                # The total time is the maximum of the two times
                total_time = max(time1, time2)
                
                if total_time < min_time:
                    min_time = total_time
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()