import sys
import math
from collections import defaultdict, deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        tree = defaultdict(list)
        for _ in range(N - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            tree[u].append(v)
            tree[v].append(u)
            idx += 2
        
        # Compute sizes of subtrees
        size = [0] * (N + 1)
        visited = [False] * (N + 1)
        
        def dfs(u, parent):
            visited[u] = True
            size[u] = 1
            for v in tree[u]:
                if not visited[v]:
                    dfs(v, u)
                    size[u] += size[v]
        
        dfs(1, -1)
        
        # Find the node with the smallest W
        min_w = float('inf')
        best_x = -1
        
        for u in range(1, N + 1):
            # The number of fighters when removing u is the maximum of the sizes of its children
            max_child_size = 0
            for v in tree[u]:
                if v != 1 and not visited[v]:  # Not the parent
                    max_child_size = max(max_child_size, size[v])
            # The other part is N - size[u]
            w = max(max_child_size, N - size[u])
            if w < min_w or (w == min_w and u < best_x):
                min_w = w
                best_x = u
        
        results.append(f"{best_x} {min_w}")
    
    print("\n".join(results))