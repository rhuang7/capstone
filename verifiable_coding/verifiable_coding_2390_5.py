import sys
import collections

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    q = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        count = collections.Counter(a)
        values = sorted(count.values(), reverse=True)
        
        res = 0
        i = 0
        while i < len(values):
            if values[i] > i + 1:
                res += i + 1
                values[i] = i + 1
            else:
                res += values[i]
                i += 1
        
        results.append(str(res))
    
    print('\n'.join(results))