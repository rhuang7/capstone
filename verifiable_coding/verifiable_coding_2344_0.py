import sys
import math
from collections import defaultdict, deque

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
        graph = defaultdict(list)
        for i in range(m):
            u = int(data[idx]) - 1
            v = int(data[idx+1]) - 1
            edges.append((u, v))
            graph[u].append((v, i))
            graph[v].append((u, i))
            idx += 2
        
        # Try to find a matching of size n
        match = []
        used = [False] * m
        def dfs(u, visited):
            for v, i in graph[u]:
                if not visited[v] and not used[i]:
                    visited[v] = True
                    used[i] = True
                    match.append(i)
                    if len(match) == n:
                        return True
                    if dfs(v, visited):
                        return True
                    visited[v] = False
                    used[i] = False
            return False
        
        visited = [False] * (3 * n)
        found = False
        for u in range(3 * n):
            if not visited[u]:
                visited = [False] * (3 * n)
                if dfs(u, visited):
                    found = True
                    break
        
        if found:
            results.append("Matching")
            results.append(' '.join(map(str, match)))
            continue
        
        # If no matching, try to find an independent set of size n
        # We use a greedy approach: select nodes with the least degree
        degrees = [0] * (3 * n)
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
        
        ind_set = []
        for i in range(3 * n):
            if len(ind_set) == n:
                break
            if degrees[i] == 0:
                ind_set.append(i)
            else:
                # Check if adding this node to the set is safe
                safe = True
                for node in ind_set:
                    if node in graph[i]:
                        safe = False
                        break
                if safe:
                    ind_set.append(i)
        
        if len(ind_set) == n:
            results.append("IndSet")
            results.append(' '.join(map(str, [x + 1 for x in ind_set])))
        else:
            results.append("Impossible")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()