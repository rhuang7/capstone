import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k, d = map(int, data[idx:idx+3])
        idx += 3
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        min_sub = float('inf')
        
        # For each possible starting position of the d-day window
        for i in range(n - d + 1):
            # Use a sliding window to track unique shows in the window
            seen = set()
            unique = 0
            for j in range(i, i + d):
                if a[j] not in seen:
                    seen.add(a[j])
                    unique += 1
            min_sub = min(min_sub, unique)
        
        results.append(str(min_sub))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()