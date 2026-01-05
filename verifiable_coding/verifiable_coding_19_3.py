import sys
import collections

def solve():
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
        
        min_subscriptions = float('inf')
        
        # For each possible starting position of a d-day window
        for i in range(n - d + 1):
            # Use a sliding window to track the unique shows in the window
            window = collections.defaultdict(int)
            unique = 0
            for j in range(i, i + d):
                show = a[j]
                if window[show] == 0:
                    unique += 1
                window[show] += 1
            min_subscriptions = min(min_subscriptions, unique)
        
        results.append(str(min_subscriptions))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()