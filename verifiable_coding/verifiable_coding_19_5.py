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
        
        min_subs = float('inf')
        
        for i in range(n - d + 1):
            show_count = collections.defaultdict(int)
            unique_shows = 0
            for j in range(i, i + d):
                show = a[j]
                if show_count[show] == 0:
                    unique_shows += 1
                show_count[show] += 1
            min_subs = min(min_subs, unique_shows)
        
        results.append(str(min_subs))
    
    print('\n'.join(results))