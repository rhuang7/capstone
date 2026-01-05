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
        n, T = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        count = collections.defaultdict(int)
        for num in a:
            count[num] += 1
        
        res = []
        for num in a:
            res.append(0)
        
        for num in a:
            if T - num in count and T - num != num:
                if count[num] > 0 and count[T - num] > 0:
                    res[a.index(num)] = 1
                    count[num] -= 1
                    count[T - num] -= 1
        
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))