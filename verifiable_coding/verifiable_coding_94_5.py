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
        n, T = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        count = collections.defaultdict(int)
        for num in a:
            count[num] += 1
        
        color = []
        for num in a:
            if T - num in count and count[T - num] > 0:
                color.append(0)
                count[T - num] -= 1
            else:
                color.append(1)
        
        results.append(' '.join(map(str, color)))
    
    print('\n'.join(results))