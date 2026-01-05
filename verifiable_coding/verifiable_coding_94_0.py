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
        
        color = [0] * n
        for i in range(n):
            num = a[i]
            if T - num in count:
                if count[num] > 0 and count[T - num] > 0:
                    color[i] = 1
                    count[num] -= 1
                    count[T - num] -= 1
                else:
                    color[i] = 0
                    count[num] -= 1
            else:
                color[i] = 0
                count[num] -= 1
        
        results.append(' '.join(map(str, color)))
    
    print('\n'.join(results))