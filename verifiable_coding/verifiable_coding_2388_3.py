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
        
        # Perform BFS to find a bipartition
        color = [-1] * (n+1)
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
                    # This should not happen in a bipartite graph
                    pass
        
        # Choose all vertices from the smaller part of the bipartition
        part0 = []
        part1 = []
        for i in range(1, n+1):
            if color[i] == 0:
                part0.append(i)
            else:
                part1.append(i)
        
        if len(part0) <= len(part1):
            res = part0
        else:
            res = part1
        
        results.append(str(len(res)))
        results.append(' '.join(map(str, res)))
    
    print('\n'.join(results))