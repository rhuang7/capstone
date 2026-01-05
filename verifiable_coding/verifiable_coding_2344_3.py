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
            u, v = edges[i]
            if not used[i]:
                for j in range(i + 1, m):
                    if edges[j][0] == v or edges[j][1] == v:
                        used[j] = True
                used[i] = True
                match.append(i + 1)
                if len(match) == n:
                    results.append("Matching")
                    results.extend(map(str, match))
                    break
        else:
            # If no matching found, try to find an independent set of size n
            # We can use a greedy approach: select vertices with the least degree
            degree = [0] * (3 * n)
            for u, v in edges:
                degree[u] += 1
                degree[v] += 1
            independent_set = []
            for i in range(3 * n):
                if len(independent_set) < n:
                    if all((i != j and (i not in independent_set or j not in independent_set)) for j in independent_set):
                        independent_set.append(i)
            if len(independent_set) == n:
                results.append("IndSet")
                results.extend(map(str, [x + 1 for x in independent_set]))
            else:
                results.append("Impossible")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()