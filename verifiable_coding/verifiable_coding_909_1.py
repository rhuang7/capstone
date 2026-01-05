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
        b = list(map(int, data[idx:idx + n]))
        idx += n
        g = list(map(int, data[idx:idx + n]))
        idx += n
        
        b.sort()
        g.sort()
        
        i = j = 0
        res = []
        while i < n and j < n:
            if b[i] <= g[j]:
                res.append(b[i])
                i += 1
            else:
                res.append(g[j])
                j += 1
        while i < n:
            res.append(b[i])
            i += 1
        while j < n:
            res.append(g[j])
            j += 1
        
        valid = True
        for k in range(len(res) - 1):
            if res[k] > res[k + 1]:
                valid = False
                break
            if (res[k] in b and res[k + 1] in b) or (res[k] in g and res[k + 1] in g):
                valid = False
                break
        
        results.append("YES" if valid else "NO")
    
    print("\n".join(results))