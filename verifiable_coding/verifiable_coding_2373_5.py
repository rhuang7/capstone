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
        
        # For each pair (i, n-i+1), find possible x values and count how many pairs can have x
        # Then find the x with the maximum number of pairs, and calculate the minimal replacements
        from collections import defaultdict
        freq = defaultdict(int)
        
        for i in range(n // 2):
            x1 = a[i]
            x2 = a[n - i - 1]
            x = x1 + x2
            if 1 <= x <= 2 * k:
                freq[x] += 1
        
        # Find the x with maximum frequency
        max_freq = 0
        best_x = 0
        for x in freq:
            if freq[x] > max_freq:
                max_freq = freq[x]
                best_x = x
        
        # Calculate the minimal replacements
        res = 0
        for i in range(n // 2):
            x1 = a[i]
            x2 = a[n - i - 1]
            if x1 + x2 != best_x:
                res += 1
        
        results.append(str(res))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()