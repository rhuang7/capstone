import sys
import collections

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        count = collections.Counter(a)
        freq = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        if freq[0][1] > (N + 1) // 2:
            results.append("No")
            continue
        
        res = [0] * N
        pos = 0
        for color, _ in freq:
            for _ in range(count[color]):
                res[pos] = color
                pos += 1
        
        if res == a:
            results.append("No")
            continue
        
        results.append("Yes")
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))