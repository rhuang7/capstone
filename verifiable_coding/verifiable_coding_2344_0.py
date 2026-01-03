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
        for _ in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            idx += 2
        
        # Try to find a matching of size n
        # We'll use a greedy approach
        match = []
        used = [False] * (3 * n)
        for i in range(m):
            u, v = edges[i]
            if not used[u] and not used[v]:
                match.append(i + 1)
                used[u] = True
                used[v] = True
                if len(match) == n:
                    results.append("Matching")
                    results.append(' '.join(map(str, match)))
                    break
        else:
            # No matching found, try to find an independent set of size n
            # We'll use a greedy approach
            indep = []
            for i in range(m):
                u, v = edges[i]
                if not (u in indep or v in indep):
                    indep.append(u)
                    indep.append(v)
                    if len(indep) == n:
                        results.append("IndSet")
                        results.append(' '.join(map(str, indep)))
                        break
            else:
                results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()