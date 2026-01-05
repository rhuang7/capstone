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
        
        # For each possible starting position of the d-day window
        for i in range(n - d + 1):
            # Use a sliding window approach to count unique shows in the window
            window = a[i:i+d]
            unique_shows = len(set(window))
            min_subscriptions = min(min_subscriptions, unique_shows)
        
        results.append(min_subscriptions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()