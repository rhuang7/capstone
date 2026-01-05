import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        edges = []
        for i in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Try to find a matching of size n
        match = []
        used = [False] * m
        for i in range(m):
            if not used[i]:
                u, v = edges[i]
                if not used[i]:
                    match.append(i)
                    used[i] = True
                    for j in range(m):
                        if j != i and (edges[j][0] == u or edges[j][0] == v or edges[j][1] == u or edges[j][1] == v):
                            used[j] = True
                    if len(match) == n:
                        break
        if len(match) == n:
            results.append("Matching")
            results.append(' '.join(map(str, [x+1 for x in match])))
            continue
        
        # If no matching, try to find an independent set of size n
        # We can use a greedy approach: pick vertices with degree <= n-1
        degrees = [0] * (3 * n)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
        ind_set = []
        for i in range(3 * n):
            if degrees[i] <= n - 1:
                ind_set.append(i)
                if len(ind_set) == n:
                    break
        if len(ind_set) == n:
            results.append("IndSet")
            results.append(' '.join(map(str, [x+1 for x in ind_set])))
            continue
        
        results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()