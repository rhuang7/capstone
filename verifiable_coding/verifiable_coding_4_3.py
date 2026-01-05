import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        res = [0] * n
        for m in range(1, n + 1):
            found = False
            for i in range(n):
                if p[i] == m:
                    found = True
                    break
            if found:
                res[m - 1] = 1
            else:
                res[m - 1] = 0
        
        results.append(''.join(map(str, res)))
    
    print('\n'.join(results))