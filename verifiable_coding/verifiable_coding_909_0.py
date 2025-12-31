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
                alternated = True
            else:
                results.append(g[j])
                j += 1
                alternated = False
        
        while i < n:
            results.append(b[i])
            i += 1
        
        while j < n:
            results.append(g[j])
            j += 1
        
        if alternated and len(results) == 2 * n:
            results = ["YES"]
        else:
            results = ["NO"]
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()