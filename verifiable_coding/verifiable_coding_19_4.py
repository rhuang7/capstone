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
        
        # Sliding window approach
        for i in range(n - d + 1):
            window = a[i:i+d]
            show_count = collections.defaultdict(int)
            for show in window:
                show_count[show] += 1
            min_subscriptions = min(min_subscriptions, len(show_count))
        
        results.append(min_subscriptions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()