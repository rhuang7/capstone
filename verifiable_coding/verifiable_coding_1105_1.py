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
        
        # Try all possible ways to assign dishes to burners
        # We consider all possible partitions of the dishes into two groups
        # and calculate the time for each partition
        
        # Generate all possible partitions of the dishes into two groups
        # (each dish is assigned to one of the two burners)
        # We use a recursive approach to generate all possible assignments
        
        # We can also use a brute-force approach for small N
        # Since N is up to 4, the total number of possible assignments is 2^4 = 16
        # So it's feasible to try all possibilities
        
        # Try all possible assignments of dishes to burners
        # Each dish can be assigned to burner 0 or 1
        # We generate all possible combinations
        from itertools import product
        
        for assignment in product([0, 1], repeat=N):
            # Calculate the total time for each burner
            burner0 = 0
            burner1 = 0
            for i in range(N):
                if assignment[i] == 0:
                    burner0 += C[i]
                else:
                    burner1 += C[i]
            # The total time is the maximum of the two burners
            total_time = max(burner0, burner1)
            if total_time < min_time:
                min_time = total_time
        
        results.append(str(min_time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()