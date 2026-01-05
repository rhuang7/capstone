import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        D = list(map(int, data[idx:idx+N]))
        idx += N
        
        res = []
        for d in D:
            if d % K == 0:
                res.append('1')
            else:
                res.append('0')
        results.append(''.join(res))
    
    print('\n'.join(results))