import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # For each pair (i, n-i+1), find possible x values and count the number of replacements needed
        # We need to find the x that requires the least replacements
        min_replacements = float('inf')
        
        # Try all possible x values (from 1 to k)
        # But since x must be such that a_i + a_j = x, and both a_i and a_j are <= k, x can be at most 2k
        # However, since a_i and a_j are already <= k, x can be at most 2k, but we can limit it to k (as per problem statement)
        # So try x from 1 to k
        for x in range(1, k+1):
            replacements = 0
            for i in range(n // 2):
                a_i = a[i]
                a_j = a[n - i - 1]
                if a_i + a_j != x:
                    # We need to replace at least one of them
                    # Check if both are already in the correct range
                    if a_i > k or a_j > k:
                        replacements += 2
                    else:
                        # At least one replacement is needed
                        replacements += 1
            min_replacements = min(min_replacements, replacements)
        
        results.append(str(min_replacements))
    
    print('\n'.join(results))