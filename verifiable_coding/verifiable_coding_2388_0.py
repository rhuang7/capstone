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
        min_deg = n
        min_vertex = -1
        for i in range(1, n+1):
            if len(adj[i]) < min_deg:
                min_deg = len(adj[i])
                min_vertex = i
        
        # Perform BFS from min_vertex to mark all reachable nodes
        visited = [False] * (n+1)
        q = deque()
        q.append(min_vertex)
        visited[min_vertex] = True
        chosen = [min_vertex]
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    chosen.append(v)
        
        # The chosen set is all nodes reachable from min_vertex
        # We need to select at most floor(n/2) nodes
        # So we can choose the first half of the chosen nodes
        k = len(chosen)
        if k > n // 2:
            chosen = chosen[:n//2]
        
        results.append(str(len(chosen)))
        results.append(' '.join(map(str, chosen)))
    
    print('\n'.join(results))