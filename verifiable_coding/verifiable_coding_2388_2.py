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
        
        # BFS to find a bipartition
        color = [-1] * (n + 1)
        q = deque()
        q.append(1)
        color[1] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    # This is not possible in a bipartite graph, but the problem says it's connected and has no odd cycles
                    pass
        
        # Choose all vertices from the smaller partition
        chosen = []
        for i in range(1, n+1):
            if color[i] == 0:
                chosen.append(i)
        
        # If the smaller partition is more than half, choose the larger one
        if len(chosen) > n // 2:
            chosen = [i for i in range(1, n+1) if color[i] == 1]
        
        results.append(str(len(chosen)))
        results.append(' '.join(map(str, chosen)))
    
    print('\n'.join(results))