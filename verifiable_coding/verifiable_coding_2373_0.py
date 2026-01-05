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
        
        # For each pair (i, n-i+1), find possible x values and count required changes
        count = {}
        for i in range(0, n, 2):
            x1 = a[i] + a[n - i - 1]
            if x1 <= 2 * k:
                count[x1] = count.get(x1, 0) + 1
        
        # Find the x with maximum count (min changes)
        max_count = -1
        best_x = None
        for x in count:
            if count[x] > max_count:
                max_count = count[x]
                best_x = x
        
        # Calculate the minimum changes needed
        min_changes = 0
        for i in range(0, n, 2):
            x = best_x
            left = a[i]
            right = a[n - i - 1]
            if left + right != x:
                min_changes += 1
        
        results.append(str(min_changes))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()