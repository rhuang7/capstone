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
        min_replacements = float('inf')
        
        # Try all possible x values (from 1 to k)
        for x in range(1, k+1):
            replacements = 0
            for i in range(n // 2):
                left = a[i]
                right = a[n - i - 1]
                if left + right != x:
                    # Need to replace at least one of them
                    # Check if both are valid
                    if left > k or right > k:
                        # Both are invalid, need to replace both
                        replacements += 2
                    else:
                        # At least one is invalid, need to replace at least one
                        replacements += 1
            min_replacements = min(min_replacements, replacements)
        
        results.append(str(min_replacements))
    
    print('\n'.join(results))