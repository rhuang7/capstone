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
        
        # For each pair (i, n-i+1), we need to find a value x such that a[i] + a[n-i+1] = x
        # We need to find the x that requires the least number of replacements
        
        # We'll try all possible x values (from 2 to 2k, since each element is at least 1 and at most k)
        # But since k can be up to 2e5, we need an efficient way to find the optimal x
        
        # Instead, we can collect all possible x values from the current pairs and try them
        # For each pair, the possible x values are between 2 and 2k, but we can collect the x values from the current pairs
        
        # Collect all possible x values from the current pairs
        possible_x = set()
        for i in range(n // 2):
            x = a[i] + a[n - i - 1]
            possible_x.add(x)
        
        # Try each possible x from the current pairs and find the one with the minimum replacements
        min_replacements = float('inf')
        for x in possible_x:
            replacements = 0
            for i in range(n // 2):
                left = a[i]
                right = a[n - i - 1]
                if left + right != x:
                    # We need to replace at least one of them
                    # The minimum number of replacements is 1 if one of them can be adjusted
                    # Otherwise, 2
                    if left != 1 and right != 1:
                        replacements += 2
                    else:
                        replacements += 1
            min_replacements = min(min_replacements, replacements)
        
        # Also check the x values that are not in the current pairs (but are possible)
        # For example, x could be 2, but the current pairs don't have that sum
        # We can try all possible x values from 2 to 2k
        # However, since k can be up to 2e5, we need to optimize
        
        # We can try all x from 2 to 2k
        for x in range(2, 2 * k + 1):
            replacements = 0
            for i in range(n // 2):
                left = a[i]
                right = a[n - i - 1]
                if left + right != x:
                    # We need to replace at least one of them
                    # The minimum number of replacements is 1 if one of them can be adjusted
                    # Otherwise, 2
                    if left != 1 and right != 1:
                        replacements += 2
                    else:
                        replacements += 1
            min_replacements = min(min_replacements, replacements)
        
        results.append(str(min_replacements))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()