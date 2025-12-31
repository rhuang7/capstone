import sys
import math
from collections import deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # BFS to find a vertex with the smallest degree
        min_degree = n
        min_vertex = -1
        for i in range(1, n+1):
            if len(adj[i]) < min_degree:
                min_degree = len(adj[i])
                min_vertex = i
        
        # Perform BFS to select vertices
        visited = [False] * (n+1)
        q = deque()
        q.append(min_vertex)
        visited[min_vertex] = True
        selected = []
        
        while q:
            u = q.popleft()
            selected.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Check if the number of selected vertices is <= n//2
        k = len(selected)
        if k > n // 2:
            # If not, select the first half of the selected vertices
            selected = selected[:n//2]
            k = len(selected)
        
        results.append(str(k))
        results.append(' '.join(map(str, selected)))
    
    print('\n'.join(results))