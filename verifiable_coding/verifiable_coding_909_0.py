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
        alternated = False
        while i < n and j < n:
            if b[i] <= g[j]:
                results.append(b[i])
                i += 1
            else:
                results.append(g[j])
                j += 1
        while i < n:
            results.append(b[i])
            i += 1
        while j < n:
            results.append(g[j])
            j += 1
        
        valid = True
        for k in range(len(results) - 1):
            if results[k] > results[k + 1]:
                valid = False
                break
            if (results[k] in b and results[k + 1] in b) or (results[k] in g and results[k + 1] in g):
                valid = False
                break
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()