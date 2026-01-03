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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Group the sequence into runs of equal elements
        runs = []
        current_val = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == current_val:
                count += 1
            else:
                runs.append(count)
                current_val = A[i]
                count = 1
        runs.append(count)
        
        # Find the minimum number of operations
        min_ops = float('inf')
        
        # Try all possible ways to make the sequence even
        # Case 1: All runs have even length
        if all(x % 2 == 0 for x in runs):
            min_ops = 0
        
        # Case 2: Change one run to even length
        for i in range(len(runs)):
            if runs[i] % 2 == 1:
                # Change this run to even length (add 1)
                new_len = runs[i] + 1
                min_ops = min(min_ops, 1)
        
        # Case 3: Remove one run (if it's odd)
        for i in range(len(runs)):
            if runs[i] % 2 == 1:
                min_ops = min(min_ops, 1)
        
        # Case 4: Remove two runs (if both are odd)
        odd_runs = [x for x in runs if x % 2 == 1]
        if len(odd_runs) >= 2:
            min_ops = min(min_ops, 2)
        
        results.append(str(min_ops))
    
    print('\n'.join(results))