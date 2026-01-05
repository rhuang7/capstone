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
        
        # Count frequency of possible x values for each pair
        from collections import defaultdict
        freq = defaultdict(int)
        for i in range(n // 2):
            x = a[i] + a[n - i - 1]
            freq[x] += 1
        
        # Find the x with the maximum frequency (least replacements needed)
        max_freq = 0
        best_x = None
        for x in freq:
            if freq[x] > max_freq:
                max_freq = freq[x]
                best_x = x
        
        # Calculate the minimum number of replacements needed for best_x
        res = 0
        for i in range(n // 2):
            left = a[i]
            right = a[n - i - 1]
            if left + right != best_x:
                res += 1
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()