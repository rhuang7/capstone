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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        S = data[idx]
        idx += 1
        
        # Preprocess the string to get positions of I, M, X, and count of : between positions
        positions = {'I': [], 'M': [], 'X': []}
        for i in range(N):
            if S[i] == 'I':
                positions['I'].append(i)
            elif S[i] == 'M':
                positions['M'].append(i)
            elif S[i] == 'X':
                positions['X'].append(i)
        
        # Precompute prefix sums of : to quickly calculate number of : between two positions
        prefix = [0] * (N + 1)
        for i in range(N):
            prefix[i+1] = prefix[i] + (1 if S[i] == ':' else 0)
        
        # Function to calculate number of : between i and j
        def count_sheets(i, j):
            return prefix[j] - prefix[i]
        
        # For each magnet, find all possible irons it can attract
        # And greedily assign irons to magnets
        # We'll use a greedy approach: for each magnet, try to assign the closest possible iron
        # that hasn't been assigned yet and satisfies the conditions
        
        # We'll use a list to keep track of which irons are already assigned
        assigned = [False] * N
        
        count = 0
        
        for m in positions['M']:
            # Try to find the closest I to the left of m
            for i in range(m-1, -1, -1):
                if S[i] == 'I' and not assigned[i]:
                    # Check if there are no X between i and m
                    has_x = False
                    for k in range(i+1, m):
                        if S[k] == 'X':
                            has_x = True
                            break
                    if not has_x:
                        # Calculate attraction power
                        dist = m - i
                        sheets = count_sheets(i, m)
                        power = K + 1 - dist - sheets
                        if power > 0:
                            assigned[i] = True
                            count += 1
                            break
            # Try to find the closest I to the right of m
            for i in range(m+1, N):
                if S[i] == 'I' and not assigned[i]:
                    # Check if there are no X between i and m
                    has_x = False
                    for k in range(m+1, i):
                        if S[k] == 'X':
                            has_x = True
                            break
                    if not has_x:
                        # Calculate attraction power
                        dist = i - m
                        sheets = count_sheets(m, i)
                        power = K + 1 - dist - sheets
                        if power > 0:
                            assigned[i] = True
                            count += 1
                            break
        
        results.append(str(count))
    
    print('\n'.join(results))